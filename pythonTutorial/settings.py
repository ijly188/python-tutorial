"""
Django settings for pythonTutorial project.

Generated by 'django-admin startproject' using Django 4.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
import datetime
import logging
import time
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-q$$sqb4dry(0(rr!sa)+l1xfz*2z3*e5_p6&_*hg!3_c2a%l*_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '*'
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'rest_framework',
    "corsheaders",
    # install app
    'blog.apps.BlogConfig',
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    # custom middleware
    'blog.middleware.SimpleMiddleware.SimpleMiddleware',
]

ROOT_URLCONF = 'pythonTutorial.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'pythonTutorial.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'blog.UserProfile'

# CSRF_USE_SESSIONS = False
# CSRF_COOKIE_HTTPONLY = False
# CORS_ALLOW_HEADERS = ('x-csrftoken', 'authorization', 'content-type')
# CORS_ORIGIN_ALLOW_ALL = True
# CSRF_TRUSTED_ORIGINS = [
#     'http://*',
#     'http://*.127.0.0.1',
#     'http://localhost:3000'
# ]

# CORS_ORIGIN_WHITELIST = [
#     'http://localhost:3000',
# ]

CORS_ALLOW_ALL_ORIGINS  = True
CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_METHODS = ('*')
CORS_ALLOW_HEADERS = ('x-csrftoken', 'authorization', 'content-type')

CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = ['http://*']

todayDate = str(time.strftime("%Y%m%d", time.localtime()))

todayLogPath = os.path.join(BASE_DIR, 'logs', todayDate)
os.makedirs(todayLogPath, exist_ok=True)

LOGGING = {
    'version': 1,
    
    'disable_existing_loggers': False, 
    
    'formatters': {
        'verbose': {
            'format': '[{asctime}] [{levelname:8}] [{module}.{funcName}] [{pathname}:{lineno:3}] {process:d}/p {thread:d}/t {message}',
            'style': '{',
        },
        
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        
        'default': {    
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs', todayDate, 'log.txt'),
            'maxBytes': 1024 * 1024 * 50,
            'backupCount': 3,
            'formatter': 'verbose',
            'encoding': 'utf-8',
        }
    },

    'loggers': {
        'django': {
            'handlers': ['default', 'console'],
            'level': 'DEBUG',
            'propagate': True, 
        },
        'collect': {     
            'handlers': ['console'],
            'level': 'INFO',
        },   
    }
}
