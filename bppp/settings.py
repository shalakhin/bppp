#-*- coding: utf-8 -*-

import os

CWD = os.path.abspath(__file__)
CWD = CWD.split(os.path.sep)[:-2]
CWD = os.path.sep.join(CWD) + os.path.sep

DEBUG = True
TEMPLATE_DEBUG = DEBUG

LOGIN_URL = "/spaceship/connect/"
LOGIN_REDIRECT_URL = '/'
LOGIN_ERROR_URL = '/failure/'
FACEBOOK_APP_ID = 'some_id'
FACEBOOK_API_SECRET = 'api_secret'
GOOGLE_OAUTH2_CLIENT_ID = 'client_id'
GOOGLE_OAUTH2_CLIENT_SECRET = 'client_secret'

FACEBOOK_EXTENDED_PERMISSIONS = ['email']

SOCIAL_AUTH_COMPLETE_URL_NAME = 'socialauth_complete'
SOCIAL_AUTH_ASSOCIATE_URL_NAME = 'socialauth_associate_complete'
SOCIAL_AUTH_DEFAULT_USERNAME = 'os'

COMMENTS_APP = 'comments'

GRAPPELLI_ADMIN_TITLE = u"Бюро почти правильного перевода (и озвучания)"

ADMINS = (
    ('Olexandr Shalakhin', 'olexandr@shalakhin.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # 'postgresql_psycopg2'
        'NAME': CWD + 'bppp.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
TIME_ZONE = 'Europe/Kiev'

# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'ru-RU'

SITE_ID = 1
USE_I18N = True
USE_L10N = False
USE_TZ = False
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''
STATIC_ROOT = CWD + 'static' + os.path.sep

# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = STATIC_URL + "grappelli/"
STATICFILES_DIRS = (
    CWD + 'media',
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = 'some_secret_key_i_will_not_reveal'
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'social_auth.backends.facebook.FacebookBackend',
    'social_auth.backends.google.GoogleOAuth2Backend',
    'social_auth.backends.google.GoogleBackend',
    'django.contrib.auth.backends.ModelBackend',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    #social auth
    'social_auth.context_processors.social_auth_by_name_backends',
    'social_auth.context_processors.social_auth_backends',
    'social_auth.context_processors.social_auth_by_type_backends',
)

ROOT_URLCONF = 'bppp.urls'
WSGI_APPLICATION = 'bppp.wsgi.application'

TEMPLATE_DIRS = (
    CWD + 'templates',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'grappelli',
    'django.contrib.admin',
    'django.contrib.flatpages',
    'django.contrib.humanize',
    'django.contrib.comments',
    'notes',
    'comments',
    'spaceship',
    'social_auth',
)

# See http://docs.djangoproject.com/en/dev/topics/logging for
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
