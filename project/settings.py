"""
Django settings for  learning_path_tracker project.

Generated by 'django-admin startproject' using Django 2.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os




# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ewpis--2nm&$8fo^#q8z+-th_6hqrnnv$1@-5!tf2k19ld1vyz'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #Third party apps
    'bootstrap4',
    'storages',


    # My apps
    'learning_path_tracker',
    'users',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'project/templates')],
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

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'project/static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'static_cdn')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media_cdn')

if not DEBUG:
    # Default file storage by drpbox
    STATICFILES_STORAGE = 'storages.backends.dropbox.DropBoxStorage'
    DEFAULT_FILE_STORAGE = 'storages.backends.dropbox.DropBoxStorage'
    DROPBOX_OAUTH2_TOKEN = 'q22EUto9UmAAAAAAAAAACkbZNNvvSuYTGjSJF1gilUujGaySwN-rbxVPp0sBM_df'
    DROPBOX_ROOT_PATH = 'media'
    DROPBOX_CONSUMER_KEY = 'gr2qulh9syswvb9'
    DROPBOX_CONSUMER_SECRET = 'nkf0czqdpam39km'


# # Simplified static file serving.
# # https://warehouse.python.org/project/whitenoise/
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

#Telling django to use custom User model
AUTH_USER_MODEL = 'users.CustomUser'

# redirect to home page after login or logout
LOGIN_REDIRECT_URL ='learning_path_tracker:home'
LOGOUT_REDIRECT_URL = 'learning_path_tracker:home'

#Heroku settings
# if os.getcwd() == '/app':
#     import dj_database_url
#     DATABASES = {
#         'dafault' : dj_database_url.config(default='postgres://localhost')
#     }
#
#     #honor the 'X-Forwarded-proto' headerfor request.is_secure().
#     SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
#
#     #Allow only heroku to host the project.
#     ALLOWED_HOSTS = ['learning-log.heroku.com']
#
#     DEBUG = False
#
# django_heroku.settings(locals())

# for email backends
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

#send sendgrid server configuration..
# EMAIL_HOST = 'smtp.sendgrid.net'
# EMAIL_HOST_USER = 'apikey'
# EMAIL_HOST_PASSWORD = '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'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True

# For gmail or google apps
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'squalporeover.ju@gmail.com'
EMAIL_HOST_PASSWORD = 'google.ju@1'
EMAIL_PORT = 587
