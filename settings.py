####
##
#
#

# =============================================================================
#
# =============================================================================

import os
from hashlib import sha256 as sha
from os import environ
from os import linesep as CRLF

from environs import Env

env = Env()
env.read_env(override=True)

APP_ENV = env.str(
    "APP_ENV",
    "prod"
    if environ.get("DETA_SPACE_APP") or environ.get("DETA_RUNTIME")
    else "dev",
)
APP_PROD, APP_DEV = "prod" == APP_ENV, "prod" != APP_ENV
DEBUG = APP_DEBUG = env.bool("APP_DEBUG", APP_DEV)
SALT = APP_SALT = env.str("APP_SALT", "my sweety")

DETA_PROJECT_KEY = env.str("DETA_PROJECT_KEY", None)
DETA_BASE_KEY = env.str("DETA_BASE_KEY", DETA_PROJECT_KEY)

TG_TOKEN = env.str("TG_TOKEN", "@_@")
TG_MODE = env.str("TG_MODE", "update")
TG_URL = env.str("TG_URL", "0.0.0.0")
TG_MAX_CONNECTION = env.int("TG_MAX_CONNECTION", 40)
TG_DROP_UPDATES = env.bool("TG_DROP_UPDATES", APP_DEBUG)
TG_PARSE_MODE = env.str("TG_PARSE_MODE", None)
TG_TIMEOUT = env.int("TG_TIMEOUT", 10)
TG_LIMIT = env.int("TG_LIMIT", 100)

# telebot.polling updates types
TG_ALLOWED_UPDATES = [
    "message",
    "edited_message",
    "channel_post",
    "edited_channel_post",
    "inline_query",
    "chosen_inline_result",
    "callback_query",
    "shipping_query",
    "poll",
    "poll_answer",
    "my_chat_member",
    "chat_member",
]

WEBHOOK_DOMAIN = env.str("WEBHOOK_DOMAIN", "0.0.0.0")
WEBHOOK_PORT = env.int("WEBHOOK_PORT", 443)

if APP_DEV:
    WH_PATH = WEBHOOK_PATH = (
        environ.get("WEBHOOK_PATH", "")
        + "/"
        + sha((TG_URL + TG_TOKEN).encode("utf-8")).hexdigest()
    )
    # print('sets WEBHOOK_PATH', WEBHOOK_PATH)
else:
    #   APP PROD
    WH_PATH = WEBHOOK_PATH = (
        environ.get("WEBHOOK_PATH", "")
        + "/"
        + sha(
            (str(os.lstat(os.path.dirname(__file__)))).encode("utf-8")
        ).hexdigest()
    )
WH_URL = WEBHOOK_URL = WEBHOOK_DOMAIN + WEBHOOK_PATH
