#!/usr/bin/env python3
####
##
#
#

# pylint:    disable=e0401
# pylint:    disable=c0112,c0116

import settings as sets
from app import app
from app import logger as log
from bot import process_pure_updates, process_updates, set_webhook

exit() if __name__ != "__main__" else ...

log.info("START")

if sets.APP_PROD:
    set_webhook()
else:
    import uvicorn

    uvicorn.run(app, host="0.0.0.0")
# uvicorn.run(app, port=443, host="0.0.0.0")
