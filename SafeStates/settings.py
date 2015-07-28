"""
Django settings for SafeStates project.

Generated by 'django-admin startproject' using Django 1.8.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import socket
from ConfigParser import ConfigParser

DEVELOPMENT_HOSTS = [
    "Dans-MacBook-Pro.local",
    "Dans-iMac.local",
]

if socket.gethostname() in DEVELOPMENT_HOSTS:
    DEVELOPMENT = True
    ALLOWED_HOSTS = []
else:
    DEVELOPMENT = False
    ALLOWED_HOSTS = [
        "alliedjet.com",
        "www.alliedjet.com",
        "alliedjetshares.com",
        "www.alliedjetshares.com",
    ]

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_LOCATION = os.path.join(BASE_DIR, "SafeStates/SafeStates.cfg")
config = ConfigParser()
config.read(CONFIG_LOCATION)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config.get("settings", "secret_key")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = DEVELOPMENT


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'livability',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'SafeStates.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'SafeStates.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
DBTYPE = config.get("settings", "db_engine")
DBNAME = config.get("settings", "db_name")
DBUSER = config.get("settings", "db_user")
DBPASSWD = config.get("settings", "db_passwd")
DBHOST = config.get("settings", "db_host")
DBPORT = config.get("settings", "db_port")

DATABASES = {
    'default': {
        'ENGINE': DBTYPE,
        'NAME': DBNAME,
        'USER': DBUSER,
        'PASSWORD': DBPASSWD,
        'HOST': DBHOST,
        'PORT': DBPORT,
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'US/Eastern'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "SafeStates/static"),
)
STATIC_URL = '/static/'
