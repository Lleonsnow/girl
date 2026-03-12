import os
from pathlib import Path

from dotenv import load_dotenv
from django.contrib.staticfiles.storage import staticfiles_storage

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'dev-secret-change-in-production')
ADMIN_SECRET_KEY = (os.environ.get('ADMIN_SECRET_KEY') or '').strip().strip("'").strip('"')

DEBUG = os.environ.get('DJANGO_DEBUG', '1') == '1'

ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')

INSTALLED_APPS = [
    'config',
    'unfold',
    'unfold.contrib.filters',
    'unfold.contrib.forms',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'config.middleware.admin_secret',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB', 'girl'),
        'USER': os.environ.get('POSTGRES_USER', 'girl'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', ''),
        'HOST': os.environ.get('POSTGRES_HOST', 'localhost'),
        'PORT': os.environ.get('POSTGRES_PORT', '5432'),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static'] if (BASE_DIR / 'static').exists() else []
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = '/admin/'

def _split_origins(env_val: str, default: str) -> list:
    return [x.strip() for x in (env_val or default).split(',') if x.strip()]

_cors_default = 'http://localhost:3000,http://127.0.0.1:3000'
CORS_ALLOWED_ORIGINS = _split_origins(os.environ.get('CORS_ALLOWED_ORIGINS'), _cors_default)
if os.environ.get('SITE_ORIGIN', '').strip():
    site_origin = os.environ.get('SITE_ORIGIN', '').strip()
    if site_origin not in CORS_ALLOWED_ORIGINS:
        CORS_ALLOWED_ORIGINS = [*CORS_ALLOWED_ORIGINS, site_origin]

_csrf_default = 'http://localhost,http://127.0.0.1,http://localhost:3000,http://127.0.0.1:3000'
CSRF_TRUSTED_ORIGINS = _split_origins(os.environ.get('CSRF_TRUSTED_ORIGINS'), _csrf_default)
if os.environ.get('SITE_ORIGIN', '').strip():
    so = os.environ.get('SITE_ORIGIN', '').strip()
    if so not in CSRF_TRUSTED_ORIGINS:
        CSRF_TRUSTED_ORIGINS = [*CSRF_TRUSTED_ORIGINS, so]

AUTHOR_NAME = os.environ.get('AUTHOR_NAME', '')
AUTHOR_PSEUDONYM = os.environ.get('AUTHOR_PSEUDONYM', '')
AUTHOR_EMAIL = os.environ.get('AUTHOR_EMAIL', '')
AUTHOR_SOCIAL_TELEGRAM = os.environ.get('AUTHOR_SOCIAL_TELEGRAM', '')
AUTHOR_SOCIAL_INSTAGRAM = os.environ.get('AUTHOR_SOCIAL_INSTAGRAM', '')
AUTHOR_SOCIAL_TIKTOK = os.environ.get('AUTHOR_SOCIAL_TIKTOK', '')
AUTHOR_SOCIAL_TWITCH = os.environ.get('AUTHOR_SOCIAL_TWITCH', '')
AUTHOR_SOCIAL_YOUTUBE = os.environ.get('AUTHOR_SOCIAL_YOUTUBE', '')
AUTHOR_SOCIAL_DISCORD = os.environ.get('AUTHOR_SOCIAL_DISCORD', '')
AUTHOR_SOCIAL_BOOSTY = os.environ.get('AUTHOR_SOCIAL_BOOSTY', '')
SITE_ORIGIN = os.environ.get('SITE_ORIGIN', '')
SITE_OWNER_NAME = os.environ.get('SITE_OWNER_NAME', '')
SITE_OWNER_NAME_EN = os.environ.get('SITE_OWNER_NAME_EN', '')
SITE_CONTACT_EMAIL = os.environ.get('SITE_CONTACT_EMAIL', '')

_site_origin = SITE_ORIGIN or 'http://localhost:3000'
UNFOLD = {
    'SITE_TITLE': 'Admin',
    'SITE_HEADER': 'Admin',
    'SITE_ORIGIN': _site_origin,
    'SITE_URL': _site_origin,
    'THEME': 'dark',
    'BORDER_RADIUS': '12px',
    'COLORS': {
        'primary': {
            '50': 'oklch(97.5% 0.02 155)',
            '100': 'oklch(94% 0.04 155)',
            '200': 'oklch(88% 0.08 155)',
            '300': 'oklch(80% 0.12 155)',
            '400': 'oklch(70% 0.16 155)',
            '500': 'oklch(62% 0.18 155)',
            '600': 'oklch(55% 0.17 155)',
            '700': 'oklch(48% 0.14 155)',
            '800': 'oklch(40% 0.11 155)',
            '900': 'oklch(32% 0.09 155)',
            '950': 'oklch(22% 0.06 155)',
        },
    },
    'STYLES': [
        lambda request: staticfiles_storage.url('css/admin.css'),
    ],
    'SCRIPTS': [
        lambda request: staticfiles_storage.url('js/particles.js'),
    ],
}
