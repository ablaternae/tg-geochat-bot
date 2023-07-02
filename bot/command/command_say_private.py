####
##
#
#

from datetime import datetime, timedelta

from bot import bot, types

# from logger import log


# @bot.message_handler(commands=["ping"], chat_types=["group", "supergroup", "gigagroup"])
@bot.message_handler(commands=["say"], chat_types=["private"])
def say(message: types.Update):
    print('SAY', message.json)
    # bot.reply_to(
    #    message,
    #    parse_mode="html",
    #    text="sync pong {:0.3f} ms".format(
    #        (datetime.now() - datetime.fromtimestamp(message.date))
    #        / timedelta(milliseconds=1)
    #    ),
    # )
    return
