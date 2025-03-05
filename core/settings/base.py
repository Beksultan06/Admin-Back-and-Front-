import os
from pathlib import Path
from datetime import timedelta
from django.utils.translation import gettext_lazy as _
from core.settings.jazzmin import JAZZMIN_SETTINGS

from dotenv import load_dotenv

load_dotenv()
DEBUG = os.environ.get('DJANGO_DEBUG', '') != 'False'
BASE_DIR = Path(__file__).resolve().parent.parent.parent
SECRET_KEY = os.environ.get("SECRET_KEY")

# CSRF_TRUSTED_ORIGINS = ["*"]

if DEBUG:
    try:
        from .development import *
    except ImportError:
        raise ImportError("Файл development.py не найден")
else:
    try:
        from .production import *
    except ImportError:
        raise ImportError("Файл production.py не найден")

THEME_APPS = [
    "jazzmin",
]

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MY_APPS = [
    # приложений
    "app.base",
    'app.news',
    "app.passport",
    'app.managers',
    "app.gallery",
    "app.metrick",
]


LIBRARY_APPS = [
    'modeltranslation',
    "rest_framework",
    "corsheaders",
    'drf_yasg',
    'ckeditor',
    'django_ckeditor_5',
]

LANGUAGES = [
    ('ru', _('Russian')),
    ('ky', _('Kyrgyz')),
]

MODELTRANSLATION_DEFAULT_LANGUAGE = 'ru'

TRANSLATABLE_MODEL_MODULES = ['app.base.models']


LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
    os.path.join(BASE_DIR, 'locale'),
]

INSTALLED_APPS = [
    *THEME_APPS,
    *DJANGO_APPS,
    *MY_APPS,
    *LIBRARY_APPS,
]

CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'  # URL to jQuery
CKEDITOR_IMAGE_BACKEND = "pillow"  # Путь к пакету Pillow для обработки изображений
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',  # Вы можете настроить свою собственную панель инструментов CKEditor
        'height': 300,
        'width': 800,
    },
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'app.metrick.middleware.VisitLoggerMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    "corsheaders.middleware.CorsMiddleware", 
]

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MODELTRANSLATION_DEFAULT_LANGUAGE = 'ru'

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        'DIRS': [os.path.join(BASE_DIR, 'frontend/build/')],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


WSGI_APPLICATION = "core.wsgi.application"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "ru"

TIME_ZONE = "Asia/Bishkek"

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')  # Для collectstatic

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'frontend/build'),  # React build содержит index.html и assets
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CORS_ALLOW_ALL_ORIGINS = True

JAZZMIN_SETTINGS=JAZZMIN_SETTINGS

CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': '100%',
        'config': {
            'language': 'en',
        },
    },
}
