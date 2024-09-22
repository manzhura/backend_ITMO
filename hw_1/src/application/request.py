import json


async def send_responce(send, status_code, response_data):
    response_body = json.dumps(response_data).encode('utf-8')
    await send({
        'type': 'http.response.start',
        'status': status_code,
        'headers': [(b'content-type', b'application/json')],
    })
    await send({
        'type': 'http.response.body',
        'body': response_body,
    })