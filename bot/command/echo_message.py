####
##
#
#

from bot import bot
from bot import logger as log
from bot import types

log.info("echo command start")


@bot.message_handler(content_types=["text"])
def message_text_echo_chat(message: types.Update):
    if message.text:
        print(f"chat echo {message.text}")
    else:
        log.warning(str(message))
        print(message)
    # print("message_echo", message)
    # bot.reply_to(message, message.text)

    from var_dump import var_dump

    var_dump(message.from_user)
    pass
