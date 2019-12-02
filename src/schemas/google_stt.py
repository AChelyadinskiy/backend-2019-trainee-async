from marshmallow import Schema
from marshmallow import fields


class STTCreateRequestSchema(Schema):
    speech = fields.Str(required=True, description='Аудиофайл с речью', )


class STTCreateResponseSchema(Schema):
    result = fields.Str(required=True, description='Полученный текст', )
