# ambenatna.settings.py

import os
import re
from pathlib import Path
import dj_database_url
import django
from django.utils.encoding import smart_str
django.utils.encoding.smart_text = smart_str

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = "fake-key093p2i9032@#@fsd"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG", "True")
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['ambenatna.herokuapp.com', 'localhost',  '127.0.0.1']
APPEND_SLASH = True
THOUSAND_SEPARATOR = ' '
ADMIN_URL = "admin/"
DEFAULT_CHARSET = 'UTF-8'
USE_THOUSAND_SEPARATOR = True
DEFAULT_CONTENT_TYPE = 'text/html'

# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.sitemaps',

]

CUSTOM_APPS = [
    "job.apps.JobConfig",
    "user.apps.UserConfig",
    "page.apps.PageConfig",
    "project.apps.ProjectConfig",
    "dash.apps.DashboardConfig",

    "blog.apps.BlogConfig",
    "message.apps.MessageConfig"
]

PACKAGES_APPS = [
    'jet.dashboard',
    'jet',
    'django_summernote',
    'django.contrib.admin',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'taggit',
    'widget_tweaks',
]

INSTALLED_APPS += CUSTOM_APPS + PACKAGES_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
]

ROOT_URLCONF = 'ambenatna.urls'
LOGIN_REDIRECT_URL = 'dashboard:dashboard'
LOGOUT_REDIRECT_URL = 'page:home'
LOGIN_URL = "account_login"
LOGOUT_URL = 'page:home'
ACCOUNT_LOGOUT_REDIRECT = 'page:home'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "ambenatna" / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],

            'debug': DEBUG,
        },
    },
]

WSGI_APPLICATION = 'ambenatna.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# password hashers
# https://docs.djangoproject.com/en/dev/ref/settings/#password-hashers
# https://docs.djangoproject.com/en/dev/topics/auth/passwords/#using-argon2-with-django

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
]

# Hashage des donnees
# https://docs.djangoproject.com/fr/3.1/ref/settings/

DEFAULT_HASHING_ALGORITHM = 'sha1'

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        'OPTIONS': {'max_similarity': 0.9}},
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {'min_length': 9}
    },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'fr-fr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DATE_INPUT_FORMATS = ('%d/%m/%Y', '%Y-%m-%d')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [BASE_DIR / "ambenatna" / "static"]

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = "user.CustomUser"


# https://docs.djangoproject.com/fr/3.2/ref/settings/#ignorable-404-urls

IGNORABLE_404_URLS = [
    re.compile(r'^/cpc/'),
    re.compile(r'^/cpanel/'),
    re.compile(r'^/favicon\.ico$'),
    re.compile(r'^/robots\.txt$'),
    re.compile(r'\.(cgi|php|pl)$'),
    re.compile(r'^/apple-touch-icon.*\.png$'),
]

DISALLOWED_USER_AGENTS = [
    re.compile(r'^NaverBot.*'),
    re.compile(r'^EmailSiphon.*'),
    re.compile(r'^SiteSucker.*'),
    re.compile(r'^sohu-search'),
]

# Configuration django-jet
# https://jet.readthedocs.io/en/latest/config_file.html

JET_THEMES = [
    {
        'theme': 'light-gray',
        'color': '#222',
        'title': 'Light Gray'
    }
]

JET_SIDE_MENU_COMPACT = True
JET_CHANGE_FORM_SIBLING_LINKS = True


# Summernote configuration
# https://github.com/summernote/django-summernote

# Show summernote with Bootstrap4
SUMMERNOTE_THEME = 'bs4'
X_FRAME_OPTIONS = "SAMEORIGIN"

SUMMERNOTE_CONFIG = {
    # Using SummernoteWidget - iframe mode, default
    'iframe': True,

    'summernote': {
        # As an example, using Summernote Air-mode
        'airMode': False,

        # Change editor size
        'width': '100%',
        'height': '300',

        # Toolbar customization
        # https://summernote.org/deep-dive/#custom-toolbar-popover
        'toolbar': [
            ['font', ['bold', 'italic', 'underline', 'clear',
                      'strikethrough', 'superscript', 'subscript']],
            ['fontname', ['fontname']],
            ['color', ['color']],
            ['para', ['ul', 'ol', 'paragraph']],
            ['table', ['table']],
            ['insert', ['link', 'video']],
            ['view', ['fullscreen', 'codeview', 'help']],
        ],

        # Set to `True` to return attachment paths in absolute URIs.
        'attachment_absolute_uri': True,

        # Require users to be authenticated for uploading attachments.
        'attachment_require_authentication': True,

        # Set custom storage class for attachments.
        'attachment_storage_class': 'utils.function_utils.upload_image_path',

        'codemirror': {
            'mode': 'htmlmixed',
            'lineNumbers': 'true',
            'theme': 'monokai',
        },
    },
}


# ACCOUNT_ADAPTER = "user.adapter.CustomAccountAdapter"

# https://docs.djangoproject.com/fr/dev/ref/settings/#login-redirect-url
# LOGIN_REDIRECT_URL = ACCOUNT_ADAPTER

# Configuration django-allauth
# https://django-allauth.readthedocs.io/en/latest/configuration.html

ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USER_MODEL_EMAIL_FIELD = 'email'
ACCOUNT_AUTHENTICATION_METHOD = 'email'
SITE_ID = 1

EMAIL_PORT = 587
EMAIL_TIMEOUT = 5
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp-relay.sendinblue.com'
EMAIL_HOST_USER = 'flavienhgs@gmail.com'
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')
DEFAULT_FROM_EMAIL = SERVER_EMAIL = 'hello@embenata.com'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

prod_db = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(prod_db)
