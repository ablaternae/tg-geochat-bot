####
##
#
#

from bot import bot, send_antiflood, types
from bot.options import BUTTON_BYE, BUTTON_HI, PHRASE_ENTERS, PHRASE_WELCOME
from bot import get_nickname
from settings import CRLF
from db.model import Statistical
from db.model.user import User


@bot.message_handler(commands=["start", "restart"], chat_types=["private"])
def start(message: types.Update):
    # "suffix": "{CRLF}and about {N} people around you\.U R not in Kansas any more\.".format(
    text = PHRASE_WELCOME.format(
        **{
            "user_id": message.from_user.id,
            "nickname": get_nickname(message.from_user),
            "suffix": f"{CRLF}Press button \u2193\u2193\u2193 to pick location",
        }
    )

    # Клавиатура с кнопкой запроса локации
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_start = types.KeyboardButton(text=BUTTON_HI, request_location=True)
    keyboard.add(button_start)
    bot.send_message(chat_id=message.chat.id, text=text, reply_markup=keyboard)

    # send_antiflood(
    # parse_mode="html",
    # message_echo(message)

    User.add_tg_user(message.from_user)
