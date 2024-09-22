import uvicorn

from src.application.request import send_responce
from src.application.route import route


async def application(scope, receive, send) -> None:

    assert scope['type'] == 'http'

    if scope['method'] == 'GET':

        await route(scope, receive, send)
    else:
        await send_responce(send, 404, 'Not found')

