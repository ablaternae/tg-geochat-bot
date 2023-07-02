####
##
##
#

import json

from fastapi import (
    Body,
    Depends,
    FastAPI,
    HTTPException,
    Path,
    Request,
    Response,
    status,
)
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse, JSONResponse

from bot import process_pure_updates, set_webhook, types
from db.logger import logger as log

# import settings as sets
from settings import WEBHOOK_PATH

app = FastAPI()


@app.on_event("startup")  # не на всех версиях работает
async def app_on_startup():
    log.info("app_on_startup")
    return set_webhook()


@app.route(
    path=WEBHOOK_PATH,
    methods=["POST"],
)
async def webhook(
    request: Request,
    # payload: dict = Body(...),
):
    dict_body = await request.json()
    # print("webhook", WEBHOOK_PATH, dict_body)

    try:
        # data = [types.Update.de_json(ju) for ju in [payload]] #   это генератор
        data = [types.Update.de_json(dict_body)]
    except Exception as e:
        print("input data error", e)
        return JSONResponse(status_code=400, content={"error": "data error"})

    # log.info("message {}".format(data.__repr__()))

    # bot.process_new_updates(data)
    process_pure_updates(data)
    #   бот синхронный, роутер асинхронный. но пока данные обрабатываются, можно вернуть ответ

    return JSONResponse(status_code=200, content={"ok": True})


@app.route(path="/docs")
@app.route(path="/redoc")
@app.route(path="/{all}")
@app.route(path="/")
async def _403(request: Request):
    # set_webhook()
    raise HTTPException(
        status_code=403,
        detail={"method": request.method, "action": "not allowed"},
    )
