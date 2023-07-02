####
##
#
#

from time import sleep
from typing import List

import settings as sets
from db.logger import logger as log
from db.model import Statistical

from ._bot import telebot, types


def set_webhook():
    if "WEBHOOK_STARTED" in dir(sets):
        log.info("webhook was started")
        return

    if sets.DEBUG or (sets.APP_PROD and "webhook" == sets.TG_MODE):
        log.info(f"WEBHOOK {sets.WEBHOOK_PATH}")
        telebot.remove_webhook()
        if not sets.APP_PROD:
            sleep(0.9)

        # Marvin's Marvellous Guide to All Things Webhook
        # https://core.telegram.org/bots/webhooks#the-short-version
        # https://core.telegram.org/bots/webhooks#testing-your-bot-with-updates

        telebot.set_webhook(
            url=sets.WEBHOOK_URL,
            # certificate=None,
            max_connections=sets.TG_MAX_CONNECTION,
            # allowed_updates=[],
            allowed_updates=sets.TG_ALLOWED_UPDATES,
            # ip_address=None,
            drop_pending_updates=(
                sets.TG_DROP_UPDATES if sets.APP_PROD else sets.APP_DEBUG
            ),
            # so it should wait as long as the maximum script execution time
            # timeout=sets.TG_TIMEOUT,  #   максимально бесполезнен
        )

        sets.WEBHOOK_STARTED = True

    return


def process_updates():
    telebot.remove_webhook()

    print("UPdates!")
    updates = telebot.get_updates(
        offset=(0 if sets.APP_DEBUG else telebot.last_update_id + 1),
        limit=0,
        allowed_updates=sets.TG_ALLOWED_UPDATES,
        timeout=sets.TG_TIMEOUT,
        long_polling_timeout=10,  #   отсутствует в async get_updates()
    )
    if sets.APP_DEBUG:
        print("len(updates)", len(updates))
        from var_dump import var_dump  # isort:skip

        # for u in updates:
        #     var_dump(u)

        print("telebot.last_update_id", telebot.last_update_id)

    telebot.process_new_updates(updates)

    if sets.TG_DROP_UPDATES:
        print("telebot.delete_webhook")
        telebot.delete_webhook(drop_pending_updates=True)

    return


def process_pure_updates(updates: List[types.Update]):
    # def process_pure_updates(updates):
    """
    trouble desc:
    https://ru.stackoverflow.com/questions/778777/telegram-bot-api-%D0%B1%D0%B5%D1%81%D0%BA%D0%BE%D0%BD%D0%B5%D1%87%D0%BD%D0%BE-%D0%BE%D1%82%D0%BF%D1%80%D0%B0%D0%B2%D0%BB%D1%8F%D0%B5%D1%82-%D0%BF%D0%BE%D0%B2%D1%82%D0%BE%D1%80%D0%BD%D1%8B%D0%B5-%D0%B7%D0%B0%D0%BF%D1%80%D0%BE%D1%81%D1%8B-%D0%BD%D0%B0-%D1%81%D0%B0%D0%B9%D1%82-%D0%BF%D1%80%D0%B8-%D0%B4%D0%BE%D0%BB%D0%B3%D0%BE-%D0%B2%D1%8B%D0%BF%D0%BE%D0%BB
    https://stackoverflow.com/questions/44950295/encountering-read-timeout-expired-error-by-webhook-after-60-sec-of-execution

    Parameters
    ----------
    updates : List[types.Update]
        DESCRIPTION.

    Returns
    -------
    None.

    """
    from db import bot_pending_updates as bpu

    for data in updates:
        print("UPD ID", data.update_id) if sets.DEBUG else ...

        if not bpu.check(data.update_id):
            bpu.update(data)
        else:
            updates.remove(data)  #   sic

    # print("len(updates) after", len(updates))

    return telebot.process_new_updates(updates) if updates else None


def async_process_single_updates(updates: List[types.Update]):
    pass


# https://pytba.readthedocs.io/ru/latest/sync_version/index.html#telebot.TeleBot.register_message_handler
def middleware_message_handler(message: types.Update, update_types=None):
    log.debug("middleware, uid {}".format(message.id)) if sets.DEBUG else ...

    s = Statistical()

    pass


def send_antiflood(
    chat_id,
    text,
    reply_to_message_id=None,
    parse_mode=sets.TG_PARSE_MODE,
    disable_web_page_preview=True,
):
    from telebot.util import antiflood as _antiflood

    if sets.APP_DEBUG:
        print("_antiflood", chat_id, text)

    return _antiflood(
        telebot.send_message,
        **{
            "chat_id": chat_id,
            "text": text,
            "parse_mode": parse_mode,
            "disable_web_page_preview": disable_web_page_preview,
            "reply_to_message_id": reply_to_message_id,
            # "reply_to_message_id": message.message_id,
        },
    )
