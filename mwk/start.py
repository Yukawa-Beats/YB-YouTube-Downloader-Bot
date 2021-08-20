from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup(
    [
        [
         InlineKeyboardButton("Join My Channel", url="https://t.me/ybdemochannel"),
         InlineKeyboardButton("INSTAGRAM", url="https://instagram.com/yukawa_beats"),
         ],[
           InlineKeyboardButton(
            "Developer", url="https://t.me/chekuthan_0405")
            ]
      ]
    )
    welcomed = f"Hi, <b>{message.from_user.first_name}</b>.\nThis is <b>YB YouTube Downloader Bot</b> by @chekuthan_0405\nHit /help for more"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
