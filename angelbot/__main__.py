import glob
import os
import sys
from pathlib import Path

import telethon.utils
from telethon import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest, JoinChannelRequest

from angelbot import LOGS, bot, tbot
from angelbot.config import Config
from angelbot.utils import load_module
from angelbot.version import __angel__ as angelver
hl = Config.HANDLER
ANGEL_PIC = Config.ALIVE_PIC or "https://telegra.ph/file/ea9e11f7c9db21c1b8d5e.mp4"

# let's get the bot ready
async def angel_bot(bot_token):
    try:
        await bot.start(bot_token)
        bot.me = await bot.get_me()
        bot.uid = telethon.utils.get_peer_id(bot.me)
    except Exception as e:
        LOGS.error(f"angelbot_SESSION - {str(e)}")
        sys.exit()


# angelbot starter...
if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    try:
        if Config.BOT_USERNAME is not None:
            LOGS.info("Checking Telegram Bot Username...")
            bot.tgbot = TelegramClient(
                "BOT_TOKEN", api_id=Config.APP_ID, api_hash=Config.API_HASH
            ).start(bot_token=Config.BOT_TOKEN)
            LOGS.info("Checking Completed. Proceeding to next step...")
            LOGS.info("🔰 Starting angelbot 🔰")
            bot.loop.run_until_complete(angel_bot(Config.BOT_USERNAME))
            LOGS.info("🔥 angelbot Startup Completed 🔥")
        else:
            bot.start()
    except Exception as e:
        LOGS.error(f"BOT_TOKEN - {str(e)}")
        sys.exit()

# imports plugins...
path = "angelbot/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))

# Extra Modules...
# extra_repo = Config.EXTRA_REPO or "https://github.com/The-angelbot/Extra"
# if Config.EXTRA == "True":
#     try:
#         os.system(f"git clone {extra_repo}")
#     except BaseException:
#         pass
#     LOGS.info("Installing Extra Plugins")
#     path = "angelbot/plugins/*.py"
#     files = glob.glob(path)
#     for name in files:
#         with open(name) as ex:
#             path2 = Path(ex.name)
#             shortname = path2.stem
#             load_module(shortname.replace(".py", ""))


# let the party begin...
LOGS.info("Starting Bot Mode !")
tbot.start()
LOGS.info("⚡ Your angelbot Is Now Working ⚡")
LOGS.info(
    "Head to @Its_angelbot for Updates. Also join chat group to get help regarding to angelbot."
)

# that's life...
async def angel_is_on():
    try:
        if Config.LOGGER_ID != 0:
            await bot.send_file(
                Config.LOGGER_ID,
                ANGEL_PIC,
                caption=f"#START \n\nDeployed Hêllẞø† Successfully\n\n**Hêllẞø† - {angelver}**\n\nType `{hl}ping` or `{hl}alive` to check! \n\nJoin [Hêllẞø† Channel](t.me/Its_angelbot) for Updates & [Hêllẞø† Chat](t.me/angelbot_chat) for any query regarding Hêllẞø†",
            )
    except Exception as e:
        LOGS.info(str(e))

# Join angelbot Channel after deploying 🤐😅
    try:
        await bot(JoinChannelRequest("@Its_angelbot"))
    except BaseException:
        pass

# Why not come here and chat??
#    try:
#        await bot(JoinChannelRequest("@angelbot_Chat"))
#    except BaseException:
#        pass


bot.loop.create_task(angel_is_on())

if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    bot.run_until_disconnected()

# angelbot
