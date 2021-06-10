import os
from pathlib import Path
import dj_database_url
# import environ
#
#
# env = environ.Env()
# environ.Env.read_env()

BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET_KEY = env('SECRET_KEY')
#
# DEBUG = env('DEBUG')
#
# ALLOWED_HOSTS = env('ALLOWED_HOSTS').split(',')
SECRET_KEY = 'django-insecure-chz1=-wfp=alv)1ukc9$kpr@07+$^j5vjy)m%i2d9^96q*c2+s'
DEBUG = False
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '.herokuapp.com']
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'tgbot',
    'tasks',
    'django_celery_beat',
    'django_celery_results'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'WeatherTelegramBot.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'WeatherTelegramBot.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'weather',
#         'HOST': 'localhost',
#         'PORT': '5432',
#         'USER': 'admin',
#         'PASSWORD': '6HbX6YLCpT',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dfkde9hare12k7',
        'HOST': 'ec2-54-216-185-51.eu-west-1.compute.amazonaws.com',
        'PORT': '5432',
        'USER': 'hkqzqtbcnybdza',
        'PASSWORD': '370e1956131f9cfb569e635c5884f72d7fa73aee45104afb9bc4f9c712af4c7b',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# The URL to use when referring to static files (where they will be served from)
STATIC_URL = '/static/'

# The absolute path to the directory where collectstatic will collect static files for deployment.
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REDIS_HOST = 'localhost'
REDIS_PORT = '6379'


# CELERY SETTINGS
# CELERY_BROKER_URL = 'redis://redis:6379/0'
# CELERY_BACKEND = 'redis://redis:6379/0'
# #
# CELERY_BROKER_URL = os.environ['REDIS_URL'],
# CELERY_BACKEND = os.environ['REDIS_URL']
# CELERY_RESULT_BACKEND = 'django-db'

CELERY_BROKER_URL = os.environ['REDIS_URL']
BROKER_POOL_LIMIT = 1
BROKER_CONNECTION_TIMEOUT = 10
CELERY_CONCURRENCY = 4
CELERY_RESULT_BACKEND = os.environ['REDIS_URL']

CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TIMEZONE = "Europe/Moscow"
CELERY_ENABLE_UTC = True
