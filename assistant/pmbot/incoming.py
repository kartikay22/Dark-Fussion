# Dark Fussion - UserBot
# Copyright (C) 2021 TeamFussion
#
# This file is a part of < https://github.com/TeamFussion/Dark-Fussion/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamFussion/Dark-Fussion/blob/main/LICENSE/>.

"""
Incoming Message(s) forwarder.
"""

from telethon import events

from . import *

# if incoming


@asst.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def on_new_mssg(event):
    incoming = event.raw_text
    who = event.sender_id
    if is_blacklisted(who):
        return
    # doesn't reply to that user anymore
    if incoming.startswith("/"):
        pass
    elif who == OWNER_ID:
        return
    else:
        xx = await event.forward_to(OWNER_ID)
        add_stuff(xx.id, who)
