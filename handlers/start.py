from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hello {message.from_user.first_name}!
I am Somali VC Music Player, an open-source bot that lets you play music in your Telegram groups.
Maintained by @somali_tech ❤
For source code Join our support group @TeLeTiPsOfficialOnTopicChat.
Use the buttons below to know more about me.
 </b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Command", url="https://telegra.ph/%F0%9D%97%96%F0%9D%97%B5%F0%9D%97%BC%F0%9D%97%B0%F0%9D%97%BC%F0%9D%97%B9%F0%9D%97%AE%F0%9D%98%81%F0%9D%98%86%F0%9D%97%A4%F0%9D%98%82%F0%9D%97%B2%F0%9D%97%B2%F0%9D%97%BB%F0%9D%97%95%F0%9D%97%BC%F0%9D%98%81-04-03",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "👥 Group", url="https://t.me/TeLeTiPsOfficialOnTopicChat"
                    ),
                    InlineKeyboardButton(
                        "💾 Source code", url="https://github.com/sangramghangale/VCPlayerBot"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Join Channel", url="https://t.me/TeLeTiPsOfficialchannel"
                    )
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
