from views import send_message
from views.google_stt import recognize


def setup_routes(app):
    """
    Устанавливает пути запросов
    :param app:
    """
    app.router.add_post('/api/pitter/v1/message', send_message)
    app.router.add_post('/api/pitter/v1/speechtotext', recognize)
