from uuid import uuid4

from aiohttp import web
from aiohttp_apispec import docs
from aiohttp_apispec import request_schema
from aiohttp_apispec import response_schema

from schemas import MessageCreateRequestSchema
from schemas import MessageCreateResponseSchema


@docs(
    tags=['SMS'], summary='Запрос отправки сообщения', description='Описание запроса',
)
@request_schema(MessageCreateRequestSchema)
@response_schema(MessageCreateResponseSchema)
async def send_message(request):
    """
    Отправляет сообщение
    :param request:
    :return:
    """
    message_id = str(uuid4())
    res = dict(
        phoneNumber=request['data']['phoneNumber'],
        text=request['data']['text'],
        messageId=message_id,
    )

    validated_games_list = MessageCreateResponseSchema().load(res)

    return web.json_response(validated_games_list)
