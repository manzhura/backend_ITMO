import json
from urllib.parse import parse_qs
from ..application.request import send_responce


async def factorial(scope, send):
    value = scope['query_string'].decode('utf-8')
    value = value.lstrip('n=')
    try:
        value = int(value)

    except ValueError:
        await send_responce(send, status_code=422, response_data="Unprocessable Entity")
        return

    if value < 0:
        await send_responce(send, status_code=400, response_data="Bad Request")
        return

    elif value == 0:
        result = 0

    else:
        result = 1
        for i in range(2, value+1):
            result *= i

    result = json.dumps({"result": result})

    await send_responce(send, status_code=200, response_data=result)

async def fibonacci(scope, send) -> None:
    value = scope['path'].split('/')[-1]
    value = value.lstrip('n=')

    try:
        value = int(value)
    except ValueError:
        await send_responce(send, status_code=422, response_data="Unprocessable Entity")
        return

    if value < 0:
        await send_responce(send, status_code=400, response_data="Bad Request")
        return
    elif value == 0:
        result = 0
    else:
        count, result = 1, 1
        for i in range(2, value):
            count, result = result, count + result

    result = json.dumps({"result": result})
    await send_responce(send, status_code=200, response_data=result)

async def mean(scope, receive, send) -> None:
    event = await receive()
    try:
        values = event.get('body', b'')
        values = json.loads(values)
    except ValueError:
        await send_responce(send, status_code=422, response_data="Unprocessable Entity")
        return

    if not isinstance(values, list):
        await send_responce(send, status_code=422, response_data="Unprocessable Entity")
        return
    else:
        try:
            if len(values) == 0:
                await send_responce(send, status_code=400, response_data="Bad Request")
                return

            numbers = [float(value) for value in values]
            result = sum(numbers) / len(numbers)
            result = json.dumps({"result": result})

            await send_responce(send, status_code=200, response_data=result)

        except ValueError:
            await send_responce(send, status_code=422, response_data="Unprocessable Entity")
            return
