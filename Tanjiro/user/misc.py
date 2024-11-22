from pyrogram import *
from pyrogram.types import *
from Tanjiro import TanjiroUb, SUDO
import asyncio
import time

@TanjiroUb.on_message(filters.command("promote", prefixes=".") & filters.user(SUDO))
async def promoting(_, message):
     global new_admin
     if message.from_user.id == TanjiroUb.me.id:
         mes = message
     else:
         mes = await message.reply_text("....")
     if not message.reply_to_message:
         return await mes.edit("use this command reply")
     reply = message.reply_to_message
     chat_id = message.chat.id
     new_admin = reply.from_user
     admin = message.from_user     
     bot_stats = await TanjiroUb.get_chat_member(chat_id, "self")
     if not bot_stats.privileges:
         return await mes.edit("opps! iam not admin")     
     elif not bot_stats.privileges.can_promote_members:
         return await mes.edit("i dont have admin rights ")   
     await mes.edit("Promoting")
     await TanjiroUb.promote_chat_member(
        message.chat.id,
        new_admin.id,
        privileges=pyrogram.types.ChatPrivileges(
        can_change_info=True,
        can_delete_messages=True,
        can_pin_messages=True,
        can_invite_users=True,
        can_manage_video_chats=True,
        can_restrict_members=True
     ))
     await mes.edit(f"Alright!! Successful promoted")


@TanjiroUb.on_message(filters.command("demote", prefixes=".") & filters.user(SUDO))
async def demote(_, message):
     global new_admin
     if message.from_user.id == TanjiroUb.me.id:
         mes = message
     else:
         mes = await message.reply_text("....")
     if not message.reply_to_message:
         return await mes.edit("use this command reply")
     reply = message.reply_to_message
     chat_id = message.chat.id
     new_admin = reply.from_user
     admin = message.from_user     
     bot_stats = await TanjiroUb.get_chat_member(chat_id, "self")
     if not bot_stats.privileges:
         return await mes.edit("hey dude iam not admin")     
     elif not bot_stats.privileges.can_promote_members:
         return await mes.edit("i dont have admin rights ")
     await mes.edit("`Proccing...`")
     await TanjiroUb.promote_chat_member(
        chat_id,
        new_admin.id,
        privileges=pyrogram.types.ChatPrivileges(
        can_change_info=False,
        can_invite_users=False,
        can_delete_messages=False,
        can_restrict_members=False,
        can_pin_messages=False,
        can_promote_members=False,
        can_manage_chat=False,
        can_manage_video_chats=False    
     ))
     await mes.edit(f"Hmm!! demoted 🥺")

@TanjiroUb.on_message(filters.command("id", prefixes=".") & filters.user(SUDO))
async def id_command(client, message):
    if message.reply_to_message:
        replied_user_id = message.reply_to_message.from_user.id
        chat_id = message.chat.id
        response_text = (
            f"**Chat ID:** `{chat_id}`\n"
            f"**Replied User ID:** `{replied_user_id}`\n"
            f"**Your User ID:** `{message.from_user.id}`"
        )
    else:
        chat_id = message.chat.id
        response_text = (
            f"**Chat ID:** `{chat_id}`\n"
            f"**Your User ID:** `{message.from_user.id}`"
        )
    await message.reply_text(response_text)

@TanjiroUb.on_message(filters.command("ban", prefixes=".") & filters.user(SUDO))
async def ban_command(client, message):
    if not message.reply_to_message:
        await message.reply_text("Reply to a user's message to ban them! 😡")
        return

    user_id_to_ban = message.reply_to_message.from_user.id
    chat_id = message.chat.id
    chat_title = message.chat.title
    reason = " ".join(message.command[1:]) if len(message.command) > 1 else "No reason provided."

    try:
        await client.kick_chat_member(chat_id, user_id_to_ban)
        response_text = (
            f"😢 User with ID `{user_id_to_ban}` has been banned from **{chat_title}**.\n"
            f"**Reason:** {reason} 🚫"
        )
        await message.reply_text(response_text)
    except Exception as e:
        await message.reply_text(f"Failed to ban user. Error: {e} 😞")

@TanjiroUb.on_message(filters.command("unban", prefixes=".") & filters.user(SUDO))
async def unban_command(client, message):
    if not message.reply_to_message:
        await message.reply_text("Reply to a user's message to unban them! 🤔")
        return

    user_id_to_unban = message.reply_to_message.from_user.id
    chat_id = message.chat.id
    chat_title = message.chat.title

    try:
        await client.unban_chat_member(chat_id, user_id_to_unban)
        response_text = (
            f"🎉 User with ID `{user_id_to_unban}` has been unbanned in **{chat_title}**!"
        )
        await message.reply_text(response_text)
    except Exception as e:
        await message.reply_text(f"Failed to unban user. Error: {e} 😔")
