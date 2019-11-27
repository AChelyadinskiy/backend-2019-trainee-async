import jwt

from exceptions import AccessTokenInvalid
from settings import RSA_PUBLIC_KEY


def access_token_required(func):
    """
    Проверка авторизации
    :param func:
    :return:
    """

    def wrapper(request):
        if not getattr(request, 'api_user', None):
            raise AccessTokenInvalid()
        return func(request)

    return wrapper


def get_token_payload(token: str) -> dict:
    """
    Получает данные из токена
    :param token:
    :return:
    """
    return jwt.decode(token, RSA_PUBLIC_KEY, algorithms='RS256')
