import os

DEBUG: bool = bool(int(os.getenv('DEBUG', 1)))  # pylint: disable=invalid-envvar-default

PROJECT_DIR: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

GOOGLE_STT_API_KEY = os.environ['GOOGLE_STT_API_KEY']
GOOGLE_STT_API_URL = "https://speech.googleapis.com/v1/speech:recognize?key={}"

APISPEC_CONF: dict = dict(
    title='Pitter async API',
    version='0.1',
    url='/api/pitter-async/swagger/apispec',
    swagger_path='/api/pitter-async/swagger',
    static_path='/api/pitter-async/swagger/static',
)
