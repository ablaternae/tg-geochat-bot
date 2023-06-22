#!/usr/bin/env python3
####
##
#
#

# pylint:    disable=e0401
# pylint:    disable=c0112,c0116

import settings as sets
from app import logger as log
from bot import process_pure_updates, process_updates, set_webhook


def main():
    if sets.APP_DEV:
        log.info("START")
        # не прекращает поток
        process_updates()

    else:
        log.info("debug NO")
        # uvicorn.run(app, host="0.0.0.0")
        # uvicorn.run(app, port=443, host="0.0.0.0")

    pass


main() if __name__ == "__main__" else ...
