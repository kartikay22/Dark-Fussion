
# Dark Fussion - UserBot
# Copyright (C) 2021 TeamFussion
# This file is a part of < https://github.com/TeamFussion/Dark-Fussion/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamFussion/Dark-Fussion/blob/main/LICENSE/>.

from . import *
from .play import queue_func


@asst.on_message(
    filters.command(["skip", f"skip@{vcusername}"])
    & filters.user(VC_AUTHS())
    & ~filters.edited
)
async def skiplife(_, message):
    mst = message.text.split(" ", maxsplit=1)
    try:
        chat = (await Client.get_chat(mst[1])).id
    except BaseException:
        chat = message.chat.id
    await queue_func(chat)


@Client.on_message(
    filters.command("skip", HNDLR)
    & filters.outgoing
    & ~filters.edited
    & ~filters.forwarded
)
async def vc_skipe(_, message):
    await skiplife(_, message)
