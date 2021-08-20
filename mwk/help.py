# Regen & Mod by @chekuthan_0405
# Pyrogram - Telegram MTProto API Client Library for Python
# Copyright (C) 2017-2020 Dan <https://github.com/delivrance>
#
# This file is part of Pyrogram.
#
# Pyrogram is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Pyrogram is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"ഹെലോ.. 🙋🏻‍♂️ഞാൻ ഒരു യൂട്യൂബ് വീഡിയോ ഡൗണ്ലോഡർ ബോട്ട് ആണ്...എന്നെ ഉണ്ടാക്കിയത് @chekuthan_0405 ആണ്.👑\nഎനിക്ക് യൂട്യൂബ് വീഡിയോ ലിങ്ക് അയച്ചു തരിക \n\n(No PlayList, Live Stream URL Supported!)🤗"
    await message.reply_text(helptxt)
