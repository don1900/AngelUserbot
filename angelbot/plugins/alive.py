import datetime
import random
import time

from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot

from angelbot.sql.gvar_sql import gvarstat
from . import *

#-------------------------------------------------------------------------------

ALIVE_TEMP = """
<b><i>🔥🔥ɦɛʟʟɮօt ɨs օռʟɨռɛ🔥🔥</b></i>

<i><b>↼ Øwñêr ⇀</i></b> : 『 <a href='tg://user?id={}'>{}</a> 』
╭──────────────
┣─ <b>» Telethon ~</b> <i>{}</i>
┣─ <b>» Hêllẞø† ~</b> <i>{}</i>
┣─ <b>» Sudo ~</b> <i>{}</i>
┣─ <b>» Uptime ~</b> <i>{}</i>
┣─ <b>» Ping ~</b> <i>{}</i>
╰──────────────
<b><i>»»» <a href='https://t.me/its_angelbot'>[ †hê Hêllẞø† ]</a> «««</i></b>
"""
#-------------------------------------------------------------------------------

@bot.on(angel_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def up(event):
    start = datetime.datetime.now()
    angel = await eor(event, "`Building Alive....`")
    uptime = await get_time((time.time() - StartTime))
    a = gvarstat("ALIVE_PIC")
    if a is not None:
        b = a.split(" ")
        c = ["https://telegra.ph/file/ea9e11f7c9db21c1b8d5e.mp4"]
        if len(b) >= 1:
            for d in b:
                c.append(d)
        PIC = random.choice(c)
    else:
        PIC = "https://telegra.ph/file/ea9e11f7c9db21c1b8d5e.mp4"
    angel_pic = PIC
    end = datetime.datetime.now()
    ling = (end - start).microseconds / 1000
    omk = ALIVE_TEMP.format(ForGo10God, ANGEL_USER, tel_ver, angel_ver, is_sudo, uptime, ling)
    await event.client.send_file(event.chat_id, file=angel_pic, caption=omk, parse_mode="HTML")
    await angel.delete()


msg = """{}\n
<b><i>🏅 𝙱𝚘𝚝 𝚂𝚝𝚊𝚝𝚞𝚜 🏅</b></i>
<b>Telethon ≈</b>  <i>{}</i>
<b>Hêllẞø† ≈</b>  <i>{}</i>
<b>Uptime ≈</b>  <i>{}</i>
<b>Abuse ≈</b>  <i>{}</i>
<b>Sudo ≈</b>  <i>{}</i>
"""
botname = Config.BOT_USERNAME

@bot.on(angel_cmd(pattern="angel$"))
@bot.on(sudo_cmd(pattern="angel$", allow_sudo=True))
async def angel_a(event):
    uptime = await get_time((time.time() - StartTime))
    am = gvarstat("ALIVE_MSG") or "<b>»» нєℓℓвσт ιѕ σиℓιиє ««</b>"
    try:
        angel = await event.client.inline_query(botname, "alive")
        await angel[0].click(event.chat_id)
        if event.sender_id == ForGo10God:
            await event.delete()
    except (noin, dedbot):
        await eor(event, msg.format(am, tel_ver, angel_ver, uptime, abuse_m, is_sudo), parse_mode="HTML")


CmdHelp("alive").add_command(
  "alive", None, "Shows the Default Alive Message"
).add_command(
  "angel", None, "Shows Inline Alive Menu with more details."
).add_warning(
  "✅ Harmless Module"
).add()
