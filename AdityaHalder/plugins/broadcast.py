import asyncio

from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.types import Message
from requests import get

from config import CMD_HANDLER as cmd
from WhyzuProject.helpers.adminHelpers import DEVS
from WhyzuProject.helpers.basic import edit_or_reply

from .help import add_command_help

while 0 < 6:
    _GCAST_BLACKLIST = get(
        "https://raw.githubusercontent.com/mrismanaziz/Reforestation/master/blacklistgcast.json"
    )
    if _GCAST_BLACKLIST.status_code != 200:
        if 0 != 5:
            continue
        GCAST_BLACKLIST = [-1001473548283, -1001390552926, -1001726206158]
        break
    GCAST_BLACKLIST = _GCAST_BLACKLIST.json()
    break

del _GCAST_BLACKLIST


@Client.on_message(filters.command("gcast", cmd) & filters.me)
async def gcast_cmd(client: Client, message: Message):
    text = (
        message.text.split(None, 1)[1]
        if len(
            message.command,
        )
        != 1
        else None
    )
    if message.reply_to_message:
        text = message.reply_to_message.text or message.reply_to_message.caption
    if not text:
        return await edit_or_reply(message, "**Berikan Sebuah Pesan atau Reply**")
    Man = await edit_or_reply(message, "`Lagi Gcast Ngentod...`")
    done = 0
    error = 0
    async for dialog in client.iter_dialogs():
        if dialog.chat.type in ("group", "supergroup"):
            chat = dialog.chat.id
            if chat not in GCAST_BLACKLIST:
                try:
                    await client.send_message(chat, text)
                    await asyncio.sleep(0.1)
                    done += 1
                except FloodWait as e:
                    await asyncio.sleep(e.value)
                    await client.send_message(chat, text)
                    done += 1
                except Exception:
                    error += 1
    await Man.edit_text(
        f"**Sukes Gcast Nih Tod Ke** `{done}` **Grup, Gagal Gcast Tod Ke** `{error}` **Grup**"
    )


@Client.on_message(filters.command("gucast", cmd) & filters.me)
async def gucast_cmd(client: Client, message: Message):
    text = (
        message.text.split(None, 1)[1]
        if len(
            message.command,
        )
        != 1
        else None
    )
    if message.reply_to_message:
        text = message.reply_to_message.text or message.reply_to_message.caption
    if not text:
        return await edit_or_reply(message, "**Berikan Sebuah Pesan atau Reply**")
    Man = await edit_or_reply(message, "`Started global broadcast to users...`")
    done = 0
    error = 0
    async for dialog in client.iter_dialogs():
        if dialog.chat.type == "private" and not dialog.chat.is_verified:
            chat = dialog.chat.id
            if chat not in DEVS:
                try:
                    await client.send_message(chat, text)
                    await asyncio.sleep(0.1)
                    done += 1
                except FloodWait as e:
                    await asyncio.sleep(e.value)
                    await client.send_message(chat, text)
                    done += 1
                except Exception:
                    error += 1
    await Man.edit_text(
        f"**Berhasil Mengirim Pesan Ke** `{done}` **chat, Gagal Mengirim Pesan Ke** `{error}` **chat**"
    )

__MODULE__ = "BROADCAST"
__HELP__ = f"""
**🥀 Gʙᴀɴ & Gᴍᴜᴛᴇ Mᴏᴅᴜʟᴇ ✨**

**ᴜsᴀɢᴇ:**
`.gcast` - ** Rᴇᴘʟʏ Tᴏ Aɴʏᴏɴᴇ Wɪᴛʜ Tʜɪs Cᴏᴍᴍᴀɴᴅ Tᴏ Gᴍᴜᴛᴇ.**

`.ungmute` - ** Rᴇᴘʟʏ Tᴏ Aɴʏᴏɴᴇ Wɪᴛʜ Tʜɪs Cᴏᴍᴍᴀɴᴅ Tᴏ UɴGᴍᴜᴛᴇ.**

`.gban` - ** Rᴇᴘʟʏ Tᴏ Aɴʏᴏɴᴇ Wɪᴛʜ Tʜɪs Cᴏᴍᴍᴀɴᴅ Tᴏ Gʙᴀɴ.**

`.ungban` - ** Rᴇᴘʟʏ Tᴏ Aɴʏᴏɴᴇ Wɪᴛʜ Tʜɪs Cᴏᴍᴍᴀɴᴅ Tᴏ UɴGʙᴀɴ.**

`.gcast` - ** Rᴇᴘʟʏ Tᴏ Aɴʏ Mᴇssᴀɢᴇ Tᴏ Gʟᴏʙᴀʟʏ Bʀᴏᴀᴅᴄᴀsᴛ**
"""
