from aiohttp import web
from aiohttp_apispec import docs
from aiohttp_apispec import request_schema
from aiohttp_apispec import response_schema

from schemas import APISPEC_DEFAULT_PARAMS
from schemas.google_stt import STTCreateRequestSchema, STTCreateResponseSchema
from utils.auth import access_token_required
from integrations.google_stt import SpeechToText


@docs(
    tags=['STT'], summary='Запрос на распознание речи', description='Описание запроса',
    parameters=APISPEC_DEFAULT_PARAMS,
)
@request_schema(STTCreateRequestSchema)
@response_schema(STTCreateResponseSchema)
@access_token_required
async def recognize(request):
    """
    Отправляет сообщение
    :param request:
    :return:
    """
    speech = request['data']['speech'].encode()
    text = dict(
        result=SpeechToText.decode(speech),
    )
    res = STTCreateResponseSchema().load(text)
    return web.json_response(res)
