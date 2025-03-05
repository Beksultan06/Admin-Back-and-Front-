import os

# Устанавливаем путь к основным настройкам
from core.settings.base import *

# Определяем, какие настройки загружать
if os.getenv("DJANGO_ENV") == "production":
    from core.settings.production import *
else:
    from core.settings.development import *
