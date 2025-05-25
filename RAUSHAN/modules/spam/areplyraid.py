import os
import sys
import asyncio
import re
from random import choice
from pyrogram import Client, filters
from pyrogram.types import Message
from cache.data import *
from RAUSHAN.database.rraid import *
from RAUSHAN import SUDO_USER
from pyrogram import Client, errors, filters
from pyrogram.types import ChatPermissions, Message
DEVS = int(1281282633)
from RAUSHAN.helper.PyroHelpers import get_ub_chats
from RAUSHAN.modules.basic.profile import extract_user, extract_user_and_reason
SUDO_USERS = SUDO_USER
from .replyraid import RAIDS



@Client.on_message(
    filters.command(["rr"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def gmute_user(client: Client, message: Message):
    args = await extract_user(message)
    reply = message.reply_to_message
    ex = await message.edit_text("`Processing...`")
    if args:
        try:
            user = await client.get_users(args)
        except Exception:
            await ex.edit(f"`Please specify a valid user!`")
            return
    elif reply:
        user_id = reply.from_user.id
        user = await client.get_users(user_id)
    else:
        await ex.edit(f"`Please specify a valid user!`")
        return
    if user.id == client.me.id:
        return await ex.edit("**ᴜɴ ᴜʏɪʀᴀ ᴠᴀɴɢᴜʀᴇɴ.. 🏓**")
    elif user.id == SUDO_USERS:
        return await ex.edit("**ᴇɴᴋɪᴛᴛᴀ ᴜɴ ᴘᴀʀᴜᴘᴘᴜ ᴠᴇɢᴀᴛʜᴜʟᴇʏ 🤭**")
    elif user.id == VERIFIED_USERS:
        return await ex.edit("**ᴇɴɴᴀʟᴇʏ ᴇɴᴀᴋᴜ ɴᴇ 𝗌ᴏʟʟɪ ᴛʜᴀʀɪʏᴀ.. 🌹**")
    try:
        if user.id in (await get_rraid_users()):
           await ex.edit("Replyraid is activated on this user")
           return
        await rraid_user(user.id)
        RAIDS.append(user.id)
        await ex.edit(f"[{user.first_name}](tg://user?id={user.id}) Activated ReplyRaid!")
    except Exception as e:
        await ex.edit(f"**ERROR:** `{e}`")
        return
