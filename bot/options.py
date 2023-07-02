####
##
##
#


import strictyaml as yaml

# В чат заходит бот test_chatme_bot (https://t.me/test_chatmeai_bot).
# PHRASE_WELCOME = "{} {} <a href='https://t.me/{}'>{}</a>.{}"
# [inline mention of a user](tg://user?id=123456789)  https://core.telegram.org/bots/api#markdownv2-style
# PHRASE_WELCOME = "{prefix} {usertype} *{nickname}* (@{username}){suffix}"

PHRASE_WELCOME = "*[{nickname}](tg://user?id={user_id})*\, _welcome to the chatter\!_{suffix}"
PHRASE_ENTERS = (
    "*[{nickname}](tg://user?id={user_id})* enters the chat! (at address:)"
)
PHRASE_LEAVES = "*[{nickname}](tg://user?id={user_id})* leaves the chat! (bye-bye sweet prince)"
# PHRASE_WELCOME = (
#     "{prefix} {usertype} *[{nickname}](tg://user?id={user_id})*{suffix}"
# )
# Чат покидает коллега [Anonimous](https://t.me/durov).
PHRASE_FAREWELL = "{prefix} {usertype} *{nickname}*{suffix}"

PHRASE_USERTYPE = ["коллега", "бот"]

IGNORED_COMMAND = ["/me", "/ping"]
IGNORED_COMMAND_PUBLIC = ["/me", "/ping"]


BUTTON_HI = " hi there ! "
BUTTON_BYE = " bye-bye "
