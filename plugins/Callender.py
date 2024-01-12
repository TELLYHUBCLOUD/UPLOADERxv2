
from pyrogram import Client, filters
import calendar
from datetime import datetime

@Client.on_message(filters.command("calendar"))
async def calendar(client, message):
    try:
        today = datetime.today()
        input_ = calendar.month(today.year, today.month)  # Use calendar.month() function
        await message.reply_text(f"{input_}")
    except Exception as err:
        await message.reply_text("Exception Occured:- " + str(err))
