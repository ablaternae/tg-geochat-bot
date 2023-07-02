####
##
#
#

from logger import log

from bot import bot, types


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
# @bot.message_handler(content_types=["text"])
# @bot.message_handler(func=lambda message: True, chat_types=["supergroup", "gigagroup"])
@bot.message_handler(
    content_types=["text"], chat_types=["group", "supergroup", "gigagroup"]
)
def message_echo_all(message: types.Update):
    if message.text:
        log.info(f"chat echo {message.text}")
        print(f"chat echo {message.text}")
    else:
        log.warning(str(message))
        print(message)
    # print("message_echo", message)
    # bot.reply_to(message, message.text)
    pass
