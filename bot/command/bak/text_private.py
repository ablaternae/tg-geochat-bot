####
##
#
#

from bot import bot, types

# from ..bot import bot, types
# from .utils import *
# from chan.db import strdateparser
# from chan import message


# https://github.com/eternnoir/pyTelegramBotAPI#message-handlers
@bot.message_handler(content_types=["text"], chat_types=["private"])
@bot.edited_message_handler(content_types=["text"], chat_types=["private"])
def handler(message: types.Update):
    from pprint import pprint
    from time import sleep

    from chan.convert_entities import parse
    from var_dump import var_dump

    # 1.
    preamble = {
        "layout": "post",
        "title": get_title(),
        #'subtitle': '',
        "date": get_date(),
        "categories": "",
        #'tags': '',
        "author": tripcode(),
    }

    # var_dump(message.entities)
    print("parse here:")
    var_dump(parse(message))
    sleep(0.5)

    # message_replay(message)
    # message_echo(message)
