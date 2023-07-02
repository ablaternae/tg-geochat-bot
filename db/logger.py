####
##
#
#

from datetime import datetime, timedelta

from deta import Deta
from loguru import logger

from settings import DETA_BASE_KEY

LOG_TTL = 60 * 60 * 1  #   hour in secs

# Initialize with a Project Key
logdb = Deta(DETA_BASE_KEY).Base("logger")

logger.info(f"LOGGER start {datetime.now().timestamp()}")


def mylogger(message: str):
    m = dict(
        zip(
            ["datetime", "message"],
            [datetime.now().isoformat(timespec="seconds", sep=" "), message]
            # [s.strip() for s in message.split("|", 2)],
        )
    )
    logdb.put(m, expire_in=LOG_TTL)


logger.add(
    mylogger,
    colorize=False,
    format="{file}:{line} {message} {level} {time:HH:mm:ss}",
)
""" format=
https://loguru.readthedocs.io/en/stable/api/logger.html The record dict
The record is just a Python dict, accessible from sinks by message.record. It contains all contextual information of the logging call (time, function, file, line, level, etc.).
"""

__all__ = (logger, LOG_TTL)
