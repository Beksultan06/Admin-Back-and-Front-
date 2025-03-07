import os
from pathlib import Path
from core.settings.base import BASE_DIR

DEBUG = True
ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}



CORS_ORIGIN_WRITELIST = (
    'http://localhost:3000',
    'http://localhost:',
)


# CORS_ORIGIN_WRITELIST= (
#     'http://localhost',
# )



CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    'http://127.0.0.1:8000'
]

CORS_ORIGIN_WHITELIST = [
    'http://localhost:3000',
    'http://127.0.0.1:8000'
]

CORS_ALLOW_HEADERS = (
    'content-disposition', 'accept-encoding',
    'content-type', 'accept', 'origin', 'Authorization', 'access-control-allow-methods',
    'Access-Control-Allow-Origin'
)

CORS_ALLOW_METHODS = (
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
)