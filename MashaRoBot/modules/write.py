from pyrogram import filters

from MashaRoBot import pbot


@pbot.on_message(filters.command("write"))
async def handwriting(_, message):
    if len(message.command) < 2:
        return await message.reply_text("» Give Some Text To Write It On My Copy...")
    m = await message.reply_text("» Wait A Sec, Let E Write That Text...")
    name = (
        message.text.split(None, 1)[1]
        if len(message.command) < 3
        else message.text.split(None, 1)[1].replace(" ", "%20")
    )
    hand = "https://apis.xditya.me/write?text=" + name
    await m.edit("Uploading...")
    await pbot.send_chat_action(message.chat.id, "upload_photo")
    await message.reply_photo(hand, caption="Wʀɪᴛᴛᴇɴ Wɪᴛʜ 🖊 Bʏ [Tezza](t.me/Tezza_robot)")
