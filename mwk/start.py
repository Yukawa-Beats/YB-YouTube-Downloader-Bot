from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup(
    [
        [
         InlineKeyboardButton("Updates Channel", url="https://t.me/mwklinks"),
         InlineKeyboardButton("Support Group", url="https://t.me/redbullfed"),
         ],[
           InlineKeyboardButton(
            "Developer", url="https://t.me/shamilnelli")
            ]
      ]
    )
    welcomed = f"Hi, <b>{message.from_user.first_name}</b>.\nThis is <b>[MwK] YouTube To TG Uploader Bot</b> by @shamilnelli\nHit /help for more"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
