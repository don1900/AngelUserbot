from . import *

@bot.on(angel_cmd(pattern="gcast ?(.*)"))
@bot.on(sudo_cmd(pattern="gcast ?(.*)", allow_sudo=True))
async def _(event):
    reply_msg = await event.get_reply_message()
    flag = event.text[-4:]
    if reply_msg:
        OwO = reply_msg
    else:
        OwO = str(event.text[7:])
    if OwO == "":
        return await eod(event, "I need something to Gcast.")
    hel_ = await eor(event, "`Gcasting message...`")
    sed = 0
    owo = 0
    if "-all" in flag:
        async for allangel in bot.iter_dialogs():
            chat = allangel.id
            angel = OwO.replace("-all", "")
            try:
                if chat != -1001496036895:
                    await bot.send_message(chat, angel)
                    owo += 1
                elif chat == -1001496036895:
                    pass
            except BaseException:
                sed += 1
    elif "-pvt" in flag:
        async for pvtangel in bot.iter_dialogs():
            if pvtangel.is_user and not pvtangel.entity.bot:
                chat = pvtangel.id
                angel = OwO.replace("-pvt", "")
                try:
                    await bot.send_message(chat, angel)
                    owo += 1
                except BaseException:
                    sed += 1
    elif "-grp" in flag:
        async for gangel in bot.iter_dialogs():
            if gangel.is_group:
                chat = gangel.id
                angel = OwO.replace("-grp", "")
                try:
                    if chat != -1001496036895:
                        await bot.send_message(chat, angel)
                        owo += 1
                    elif chat == -1001496036895:
                        pass
                except BaseException:
                    sed += 1
    else:
        return await hel_.edit("Please give a flag to Gcast message. \n\n**Available flags are :** \n• -all : To Gcast in all chats. \n• -pvt : To Gcast in private chats. \n• -grp : To Gcast in groups.")
    UwU = sed + owo
    if flag == "-all":
        omk = "Chats"
    elif flag == "-pvt":
        omk = "PM"
    elif flag == "-grp":
        omk = "Groups"
    await hel_.edit(f"**Gcast Executed Successfully !!** \n\n**📍 Sent in :** `{owo} {omk}`\n**📍 Failed in :** `{sed} {omk}`\n**📍 Total :** `{UwU} {omk}`")

# This is a bad way. but works just fine (*﹏*;)

CmdHelp("gcast").add_command(
  "gcast", "<text/reply> <flag>", "Globally Broadcast the replied or given message based on flag given.", f"gcast Angelo -all / {hl}gcast Angelo -grp / {hl}gcast Angelo -pvt"
).add_info(
  "Global Broadcast. \n**🚩 Flags :** `-all`, `-pvt`, `-grp`"
).add_warning(
  "✅ Harmless Module."
).add()
