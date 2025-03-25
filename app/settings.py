import os
from pathlib import Path

import dj_database_url
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Define o modo de execução da aplicação
MODE = os.getenv('MODE')

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure')
DEBUG = os.getenv('DEBUG', 'False')
ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = [
    'http://localhost:3000',
    'http://localhost:8000',
]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary_storage',
    'cloudinary',
    'corsheaders',
    'django_extensions',
    'django_filters',
    'drf_spectacular',
    'rest_framework',
    'core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOW_ALL_ORIGINS = True

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'app.wsgi.application'

# Databases
DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///db.sqlite3',
        conn_max_age=600,
        conn_health_checks=True,
    )
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators
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
# https://docs.djangoproject.com/en/4.2/topics/i18n/
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
STATIC_URL = 'static/'

# App Uploader settings
MEDIA_ENDPOINT = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
FILE_UPLOAD_PERMISSIONS = 0o640

if MODE == 'DEVELOPMENT':
    MY_IP = os.getenv('MY_IP', '127.0.0.1')
    MEDIA_URL = f'http://{MY_IP}:19003/media/'
else:
    MEDIA_URL = '/media/'
    CLOUDINARY_URL = os.getenv('CLOUDINARY_URL')
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STORAGES = {
        'default': {
            'BACKEND': 'cloudinary_storage.storage.MediaCloudinaryStorage',
        },
        'staticfiles': {
            'BACKEND': 'whitenoise.storage.CompressedManifestStaticFilesStorage',
        },
    }

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SPECTACULAR_SETTINGS = {
    'TITLE': '<PROJETO> API',
    'DESCRIPTION': 'API para o projeto <descreva aqui seu projeto>.',
    'VERSION': '1.0.0',
}

AUTH_USER_MODEL = 'core.User'

REST_FRAMEWORK = {
    # "DEFAULT_AUTHENTICATION_CLASSES": ("core.authentication.TokenAuthentication",),
    # "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly",),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'PAGE_SIZE': 10,
}

PASSAGE_APP_ID = os.getenv('PASSAGE_APP_ID', 'app_id')
PASSAGE_API_KEY = os.getenv('PASSAGE_API_KEY', 'api_key')
PASSAGE_AUTH_STRATEGY = 2

print(f'{MODE = } \n{MEDIA_URL = } \n{DATABASES = }')
