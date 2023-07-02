####
##
#
#

from typing import Union

from deta import Deta  # Import Deta

from bot import types
from settings import DETA_BASE_KEY

# from datetime import datetime, timedelta

PENDING_TTL = 60 * 30  #   1/2 hour

updadb = Deta(DETA_BASE_KEY).Base("bot_pending_updates")


def check(key: Union[int, str, types.Update]):
    return bool(find(key))


def find(key: Union[int, str, types.Update]):
    return updadb.get(
        key=str(key.update_id if isinstance(key, types.Update) else key)
    )


def update(update: Union[int, str, types.Update]):
    if isinstance(update, types.Update):
        return updadb.put(
            {"text": update.message.text, "value": str(update)},
            # update TypeError: Object of type Update is not JSON serializable
            # dict(update) TypeError: 'Update' object is not iterable
            key=str(update.update_id),
            expire_in=PENDING_TTL,
        )
    else:
        return updadb.put(
            key=str(update.update_id),
            expire_in=PENDING_TTL,
        )


__all__ = ("check", "find", "update", "PENDING_TTL")
