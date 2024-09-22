import json
from  ..service.process import factorial, fibonacci, mean
from ..application.request import send_responce


async def route(scope, receive, send):

    path = scope['path']
    if path == '/factorial':

        await factorial(scope, send)

    elif path.startswith('/fibonacci'):

        await fibonacci(scope, send)

    elif path == '/mean':
        await mean(scope, receive, send)

    else:
        await send_responce(send, 404, 'Not found')
