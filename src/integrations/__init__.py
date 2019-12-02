from typing import Callable
from typing import List
from .google_stt import SpeechToText

INTEGRATIONS: List[Callable] = []

__all__ = [
    'INTEGRATIONS',
    'SpeechToText'
]
