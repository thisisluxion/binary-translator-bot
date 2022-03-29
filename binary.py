from pyrogram import Client, filters
from pyrogram.types import (InlineQueryResultArticle, InputTextMessageContent,
                            InlineKeyboardMarkup, InlineKeyboardButton)
import os
app = Client("binary_translator_bot",
              api_id=os.environ["API_ID"],
              api_hash=os.environ["API_HASH"],
             bot_token=os.environ["BOT_TOKEN"])

@app.on_inline_query()
def converter(client,inline_query):
    check = True
    for c in inline_query.query:
        if c != '0' and c != '1' and c != ' ':
            check = False
    if check is True:
        text = "".join(inline_query.query.split())
        text = ''.join(chr(int(text[i*8:i*8+8],2)) for i in range(len(text)//8))
        inline_query.answer(
            results=[
                InlineQueryResultArticle(
                    title=text,
                    input_message_content=InputTextMessageContent(
                        text
                    )
                )
            ],
            cache_time=1
        )
    else:
        #text = ' '.join(format(ord(c), 'b') for c in inline_query.query)
        text = (' '.join(bin(ord(c)) for c in inline_query.query).replace('b','')).replace(' 0100000 ', ' 00100000 ')
        inline_query.answer(
            results=[
                InlineQueryResultArticle(
                    title=text,
                    input_message_content=InputTextMessageContent(
                        text
                    )
                )
            ],
            cache_time=1
        )
app.run()

