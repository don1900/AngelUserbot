import asyncio
import time

from telethon.tl.types import DocumentAttributeAudio
from youtube_dl import YoutubeDL
from youtube_dl.utils import (
    ContentTooShortError,
    DownloadError,
    ExtractorError,
    GeoRestrictedError,
    MaxDownloadsReached,
    PostProcessingError,
    UnavailableVideoError,
    XAttrMetadataError,
)
from telethon.errors.rpcerrorlist import YouBlockedUserError

from . import *


@bot.on(angel_cmd(pattern="song ?(.*)"))
@bot.on(sudo_cmd(pattern="song ?(.*)", allow_sudo=True))
async def _(event):
    query = event.text[6:]
    max_results = 1
    if query == "":
        return await eod(event, "__Please give a song name to search.__")
    angel = await eor(event, f"__Searching for__ `{query}`")
    hel_ = await song_search(event, query, max_results, details=True)
    x, title, views, duration, thumb = hel_[0], hel_[1], hel_[2], hel_[3], hel_[4]
    thumb_name = f'thumb{ForGo10God}.jpg'
    thumbnail = requests.get(thumb, allow_redirects=True)
    open(thumb_name, 'wb').write(thumbnail.content)
    url = x.replace("\n", "")
    try:
        await angel.edit("**Fetching Song**")
        with YoutubeDL(song_opts) as somg:
            angel_data = somg.extract_info(url)
    except DownloadError as DE:
        return await eod(angel, f"`{str(DE)}`")
    except ContentTooShortError:
        return await eod(angel, "`The download content was too short.`")
    except GeoRestrictedError:
        return await eod(angel, "`Video is not available from your geographic location due to geographic restrictions imposed by a website.`")
    except MaxDownloadsReached:
        return await eod(angel, "`Max-downloads limit has been reached.`")
    except PostProcessingError:
        return await eod(angel, "`There was an error during post processing.`")
    except UnavailableVideoError:
        return await eod(angel, "`Media is not available in the requested format.`")
    except XAttrMetadataError as XAME:
        return await eod(angel, f"`{XAME.code}: {XAME.msg}\n{XAME.reason}`")
    except ExtractorError:
        return await eod(angel, "`There was an error during info extraction.`")
    except Exception as e:
        return await eod(angel, f"{str(type(e)): {str(e)}}")
    c_time = time.time()
    await angel.edit(f"**🎶 Preparing to upload song 🎶 :** \n\n{angel_data['title']} \n**By :** {angel_data['uploader']}")
    await event.client.send_file(
        event.chat_id,
        f"{angel_data['id']}.mp3",
        supports_streaming=True,
        caption=f"**✘ Song -** `{title}` \n**✘ Views -** `{views}` \n**✘ Duration -** `{duration}` \n\n**✘ By :** {angel_mention}",
        thumb=thumb_name,
        attributes=[
            DocumentAttributeAudio(
                duration=int(angel_data["duration"]),
                title=str(angel_data["title"]),
                performer=perf,
            )
        ],
        progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
            progress(d, t, event, c_time, "Uploading..", f"{angel_data['title']}.mp3")
        ),
    )
    await angel.delete()
    os.remove(f"{angel_data['id']}.mp3")


@bot.on(angel_cmd(pattern="vsong ?(.*)"))
@bot.on(sudo_cmd(pattern="vsong ?(.*)", allow_sudo=True))
async def _(event):
    query = event.text[7:]
    max_results = 1
    if query == "":
        return await eod(event, "__Please give a song name to search.__")
    angel = await eor(event, f"__Searching for__ `{query}`")
    hel_ = await song_search(event, query, max_results, details=True)
    x, title, views, duration, thumb = hel_[0], hel_[1], hel_[2], hel_[3], hel_[4]
    thumb_name = f'thumb{ForGo10God}.jpg'
    thumbnail = requests.get(thumb, allow_redirects=True)
    open(thumb_name, 'wb').write(thumbnail.content)
    url = x.replace("\n", "")
    try:
        await angel.edit("**Fetching Video**")
        with YoutubeDL(video_opts) as somg:
            angel_data = somg.extract_info(url)
    except DownloadError as DE:
        return await eod(angel, f"`{str(DE)}`")
    except ContentTooShortError:
        return await eod(angel, "`The download content was too short.`")
    except GeoRestrictedError:
        return await eod(angel, "`Video is not available from your geographic location due to geographic restrictions imposed by a website.`")
    except MaxDownloadsReached:
        return await eod(angel, "`Max-downloads limit has been reached.`")
    except PostProcessingError:
        return await eod(angel, "`There was an error during post processing.`")
    except UnavailableVideoError:
        return await eod(angel, "`Media is not available in the requested format.`")
    except XAttrMetadataError as XAME:
        return await eod(angel, f"`{XAME.code}: {XAME.msg}\n{XAME.reason}`")
    except ExtractorError:
        return await eod(angel, "`There was an error during info extraction.`")
    except Exception as e:
        return await eod(angel, f"{str(type(e)): {str(e)}}")
    c_time = time.time()
    await angel.edit(f"**📺 Preparing to upload video 📺 :** \n\n{angel_data['title']}\n**By :** {angel_data['uploader']}")
    await event.client.send_file(
        event.chat_id,
        f"{angel_data['id']}.mp4",
        supports_streaming=True,
        caption=f"**✘ Video :** `{title}` \n\n**✘ By :** {angel_mention}",
        thumb=thumb_name,
        progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
            progress(d, t, event, c_time, "Uploading..", f"{angel_data['title']}.mp4")
        ),
    )
    await angel.delete()
    os.remove(f"{angel_data['id']}.mp4")


@bot.on(angel_cmd(pattern="lyrics(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="lyrics(?: |$)(.*)", allow_sudo=True))
async def nope(kraken):
    angel = kraken.text[8:]
    uwu = await eor(kraken, f"Searching lyrics for  `{angel}` ...")
    if not angel:
        if kraken.is_reply:
            (await kraken.get_reply_message()).message
        else:
            await eod(uwu, "Give song name to get lyrics...")
            return
    troll = await bot.inline_query("iLyricsBot", f"{(deEmojify(angel))}")
    owo = await troll[0].click(Config.LOGGER_ID)
    await asyncio.sleep(3)
    owo_id = owo.id
    lyri = await bot.get_messages(entity=Config.LOGGER_ID, ids=owo_id)
    await bot.send_message(kraken.chat_id, lyri)
    await uwu.delete()
    await owo.delete()


@bot.on(angel_cmd(pattern="lsong ?(.*)"))
@bot.on(sudo_cmd(pattern="lsong ?(.*)", allow_sudo=True))
async def _(event):
    angel_ = event.text[6:]
    if angel_ == "":
        return await eor(event, "Give a song name to search")
    angel = await eor(event, f"Searching song `{angel_}`")
    somg = await event.client.inline_query("Lybot", f"{(deEmojify(angel_))}")
    if somg:
        fak = await somg[0].click(Config.LOGGER_ID)
        if fak:
            await bot.send_file(
                event.chat_id,
                file=fak,
                caption=f"**Song by :** {angel_mention}",
            )
        await angel.delete()
        await fak.delete()
    else:
        await angel.edit("**ERROR 404 :** __NOT FOUND__")


@bot.on(angel_cmd(pattern="wsong ?(.*)"))
async def _(event):
    if not event.reply_to_msg_id:
        return await eor(event, "Reply to a mp3 file.")
    rply = await event.get_reply_message()
    chat = "@auddbot"
    angel = await eor(event, "Trying to identify song...")
    async with event.client.conversation(chat) as conv:
        try:
            first = await conv.send_message("/start")
            second = await conv.get_response()
            third = await conv.send_message(rply)
            fourth = await conv.get_response()
            if not fourth.text.startswith("Audio received"):
                await angel.edit(
                    "Error identifying audio."
                )
                await event.client.delete_messages(conv.chat_id, [first.id, second.id, third.id, fourth.id])
                return
            await angel.edit("Processed...")
            fifth = await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            return await angel.edit("Please unblock @auddbot and try again")
    audio = f"**Song Name : **{fifth.text.splitlines()[0]}\n\n**Details : **__{result.text.splitlines()[2]}__"
    await angel.edit(audio)
    await event.client.delete_messages(conv.chat_id, [first.id, second.id, third.id, fourth.id, fifth.id])


CmdHelp("songs").add_command(
  "song", "<song name>", "Downloads the song from YouTube."
).add_command(
  "vsong", "<song name>", "Downloads the Video Song from YouTube."
).add_command(
  "lsong", "<song name>", "Sends the searched song in current chat.", "lsong Alone"
).add_command(
  "wsong", "<reply to a song file>", "Searches for the details of replied mp3 song file and uploads it's details."
).add_command(
  "lyrics", "<song name>", "Gives the lyrics of that song.."
).add_info(
  "Songs & Lyrics."
).add_warning(
  "✅ Harmless Module."
).add()
