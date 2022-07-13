


import os
import time
import psutil
import shutil
import string
import asyncio
from pyrogram import Client, filters
from asyncio import TimeoutError
from pyrogram.errors import MessageNotModified
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery, ForceReply
from Uploader.config import Config
from Uploader.script import Translation
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Uploader.database.database import db
from Uploader.functions.forcesub import handle_force_subscribe


@Client.on_message(
    filters.command("start") & filters.private,
)
async def start_bot(_, m: Message, lname):
    if not await db.is_user_exist(m.from_user.id):
           await db.add_user(m.from_user.id)
	   await bot.send_message(
		   Config.LOG_CHANNEL,
	           f"#NEW_USER: \n\nNew User [{m.from_user.first_name}](tg://user?id={m.from_user.id}) started @{Config.BOT_USERNAME} !!")
    return await m.reply_text(
        Translation.START_TEXT.format(m.from_user.first_name),
        reply_markup=Translation.START_BUTTONS,
        disable_web_page_preview=True,
        quote=True,
    )


@Client.on_message(
    filters.command("help") & filters.private,
)
async def help_bot(_, m: Message):
    if not await db.is_user_exist(m.from_user.id):
           await db.add_user(m.from_user.id)
	   await bot.send_message(
		   Config.LOG_CHANNEL,
	           f"#NEW_USER: \n\nNew User [{m.from_user.first_name}](tg://user?id={m.from_user.id}) started @{Config.BOT_USERNAME} !!")
    return await m.reply_text(
        Translation.HELP_TEXT,
        reply_markup=Translation.HELP_BUTTONS,
        disable_web_page_preview=True,
    )

@Client.on_message(
    filters.private & filters.reply & filters.text
)
async def edit_caption(bot, update):
    if not await db.is_user_exist(update.from_user.id):
           await db.add_user(update.from_user.id)
	   await bot.send_message(
		   Config.LOG_CHANNEL,
	           f"#NEW_USER: \n\nNew User [{update.from_user.first_name}](tg://user?id={update.from_user.id}) started @{Config.BOT_USERNAME} !!")
    try:
        await bot.send_cached_media(
            chat_id=update.chat.id,
            file_id=update.reply_to_message.video.file_id,
            reply_to_message_id=update.id,
            caption=update.text
        )
    except:
        try:
            await bot.send_cached_media(
                chat_id=update.chat.id,
                file_id=update.reply_to_message.document.file_id,
                reply_to_message_id=update.id,
                caption=update.text
            )
        except:
            pass


@Client.on_message(
    filters.private & filters.command(["addcaption"])
)

async def add_caption_help(bot, update):
    if not await db.is_user_exist(update.from_user.id):
           await db.add_user(update.from_user.id)
	   await bot.send_message(
		   Config.LOG_CHANNEL,
	           f"#NEW_USER: \n\nNew User [{update.from_user.first_name}](tg://user?id={update.from_user.id}) started @{Config.BOT_USERNAME} !!")
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ADD_CAPTION_HELP,
        #parse_mode="html",
        reply_to_message_id=update.id
    )

