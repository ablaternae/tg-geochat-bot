####
##
#
#

from bot import bot
from bot import logger as log
from bot import types


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
# @bot.message_handler(content_types=["text"])
# @bot.message_handler(content_types=["text"], chat_types=["channel"])
# @bot.message_handler(func=lambda message: True, chat_types="channel")
# @bot.message_handler(func=lambda message: "channel" == message.chat.type)
@bot.channel_post_handler(content_types=["text"])
def message_echo_chan(message: types.Update):
    bot.send_chat_action(message.chat.id, "typing")
    if message.text:
        log.info(f"channel echo {message.text}")
        print(f"channel echo {message.text}")
    else:
        log.warning(str(message))
        print(message)
    # print("message_echo", message)
    # bot.reply_to(message, message.text)
    pass
