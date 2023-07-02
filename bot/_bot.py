####
##
#
#

from telebot import TeleBot, types

from settings import APP_DEBUG, APP_PROD, TG_PARSE_MODE, TG_TOKEN

# from telebot.util import antiflood


# from telebot.async_telebot import AsyncTeleBot
# telebot = AsyncTeleBot(
#     TG_TOKEN,
#     parse_mode=TG_PARSE_MODE,
#     threaded=not APP_DEBUG,
#     disable_web_page_preview=True,
# )

telebot = TeleBot(
    TG_TOKEN,
    parse_mode=TG_PARSE_MODE,
    threaded=APP_PROD,
    disable_web_page_preview=True,
)


def get_nickname(user: types.User) -> str:
    return user.full_name.strip() or user.username.strip() or "Anonymous"


def get_userlink(user: types.User) -> str:
    return "[{nickname}](tg://user?id={user_id})".format(
        nickname=get_nickname(user), user_id=user.id
    )


__all__ = ("telebot", "types", "get_nickname", "get_userlink")
