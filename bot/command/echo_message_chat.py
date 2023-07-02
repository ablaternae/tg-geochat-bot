####
##
#
#

from bot import bot
from bot import logger as log
from bot import types

log.info("channel echo command start")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
# @bot.message_handler(content_types=["text"])
@bot.message_handler(chat_types=["group", "supergroup", "gigagroup"])
def message_text_echo_chat(message: types.Update):
    if "forward_from_chat" in message and message.is_automatic_forward:
        #   это пересылка из канала в чат
        log.info(f"chat message is forward. exit()")
        return
    if (
        "message_thread_id" in message
        and message.reply_to_message == message.message_thread_id
    ):
        #   это камент в канале
        pass
    if message.text:
        print(f"chat echo {message.text}")
    else:
        log.warning(str(message))
        print(message)
    # print("message_echo", message)
    # bot.reply_to(message, message.text)
    pass
