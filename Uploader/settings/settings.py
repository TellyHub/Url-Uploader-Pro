

import asyncio
from pyrogram import types, errors, enums
from Uploader.config import Config
from Uploader.database.database import db

async def OpenSettings(m: "types.Message"):
    try:
        await m.edit
            usr_id = m.chat.id
            user_data = await db.get_user_data(usr_id)
            if not user_data:
                await m.edit("Failed to fetch your data from database!")
                return
            upload_as_doc = user_data.get("upload_as_doc", False)
            caption = user_data.get("caption", None)
            apply_caption = user_data.get("apply_caption", True)
            thumbnail = user_data.get("thumbnail", None)
            buttons_markup = [
                [types.InlineKeyboardButton(f"ᴜᴘʟᴏᴀᴅ ᴀs {'🎥 ᴠɪᴅᴇᴏ' if upload_as_doc else '🗃️ ғɪʟᴇ'}",
                                            callback_data="triggerUploadMode")],
                [types.InlineKeyboardButton(f"{'ᴄʜᴀɴɢᴇ' if thumbnail else '🌃 sᴇᴛ'} ᴛʜᴜᴍʙɴᴀɪʟ",
                                            callback_data="setThumbnail")]
            ]
            if thumbnail:
                buttons_markup.append([types.InlineKeyboardButton("🌆 sʜᴏᴡ ᴛʜᴜᴍʙɴᴀɪʟ",
                                                          callback_data="showThumbnail")])
            buttons_markup.append([types.InlineKeyboardButton("♨️ ᴄʟᴏsᴇ",
                                                      callback_data="close")])
    except MessageNotModified:
        pass
    except FloodWait as e:
        await asyncio.sleep(e.x)
        await m.edit("You Are Spamming!")
    except Exception as err:
        raise err



