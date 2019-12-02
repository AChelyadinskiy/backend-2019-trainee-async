from aiohttp import web
from aiohttp_apispec import docs
from aiohttp_apispec import request_schema
from aiohttp_apispec import response_schema
from schemas.google_stt import STTCreateRequestSchema, STTCreateResponseSchema
from integrations.google_stt import SpeechToText


@docs(
    tags=['STT'], summary='Запрос на преобразование речи в текст', description='Описание запроса',
)
@request_schema(STTCreateRequestSchema)
@response_schema(STTCreateResponseSchema)
async def recognize(request):
    """
    Преобразует аудиофайл в текст
    :param request:
    :return:
    """
    speech = request['data']['speech'].encode()
    text = dict(
        result=await SpeechToText.decode(speech),
    )
    res = STTCreateResponseSchema().load(text)
    return web.json_response(res)
