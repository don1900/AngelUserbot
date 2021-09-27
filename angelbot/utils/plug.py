import asyncio
import datetime
import importlib
import inspect
import logging
import math
import os
import re
import sys
import time
import traceback
from pathlib import Path
from time import gmtime, strftime

from telethon import events
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.types import ChannelParticipantAdmin, ChannelParticipantCreator

from angelbot import *
from angelbot.helpers import *
from angelbot.config import *
from angelbot.utils import *


# ENV
ENV = bool(os.environ.get("ENV", False))
if ENV:
    from angelbot.config import Config
else:
    if os.path.exists("Config.py"):
        from Config import Development as Config


# load plugins
def load_module(shortname):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        import angelbot.utils

        path = Path(f"angelbot/plugins/{shortname}.py")
        name = "angelbot.plugins.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        LOGS.info("angelbot - Successfully imported " + shortname)
    else:
        import angelbot.utils

        path = Path(f"angelbot/plugins/{shortname}.py")
        name = "angelbot.plugins.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.bot = Angel
        mod.angelbot = angelbot
        mod.tbot = angelbot
        mod.Angel = Angel
        mod.tgbot = bot.tgbot
        mod.command = command
        mod.logger = logging.getLogger(shortname)
        # support for uniborg
        sys.modules["uniborg.util"] = angelbot.utils
        mod.Config = Config
        mod.borg = Angel
        mod.angelbot = Angel
        mod.edit_or_reply = edit_or_reply
        mod.eor = edit_or_reply
        mod.delete_angel = delete_angel
        mod.eod = delete_angel
        mod.Var = Config
        mod.admin_cmd = angel_cmd
        mod.angel_cmd = angel_cmd
        # support for other userbots
        sys.modules["userbot.utils"] = angelbot.utils
        sys.modules["userbot"] = angelbot
        # support for paperplaneextended
        sys.modules["userbot.events"] = angelbot
        spec.loader.exec_module(mod)
        # for imports
        sys.modules["angelbot.plugins." + shortname] = mod
        LOGS.info("⚡ Hêllẞø† ⚡ - Successfully Imported " + shortname)


# remove plugins
def remove_plugin(shortname):
    try:
        try:
            for i in LOAD_PLUG[shortname]:
                bot.remove_event_handler(i)
            del LOAD_PLUG[shortname]

        except BaseException:
            name = f"angelbot.plugins.{shortname}"

            for i in reversed(range(len(bot._event_builders))):
                ev, cb = bot._event_builders[i]
                if cb.__module__ == name:
                    del bot._event_builders[i]
    except BaseException:
        raise ValueError

# angelbot
