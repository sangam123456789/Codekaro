"""
Django settings for Codekaro project.

Generated by 'django-admin startproject' using Django 3.2.19.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path
import warnings
import dj_database_url
import django
from django.utils.encoding import force_str
django.utils.encoding.force_text = force_str
# import pymysql
# pymysql.install_as_MySQLdb()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# file_path = os.path.join(BASE_DIR, 'dbbackup', 'loggin_config.yaml')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# Use sendmail as email backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'codesniper112233@gmail.com'
EMAIL_HOST_PASSWORD = 'jttuaspzbncxqmee'



# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-xcr5-mcm&i9a9cl-!i(14syzp6kjp6!s3#jq34=kkngqui_1$n'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'Home',
    'user_agents',
    'django.contrib.admin',
    'django.contrib',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'Home.middleware.VisitorCounterMiddleware',
]

ROOT_URLCONF = 'Codekaro.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'Codekaro.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }

    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'HOST': 'containers-us-west-101.railway.app',
    #     'NAME': 'railway',
    #     'USER': 'postgres',
    #     'PASSWORD': 'xsXWpwCklC4ePTOii9eq',
    #     'PORT': '6542',

    # }     

    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'HOST': 'sql312.infinityfree.com',
    #     'NAME': 'if0_34766562_Codesniper',
    #     'USER': 'if0_34766562',
    #     'PASSWORD': 'n2SsJlE3Uw1WFxh',
    #     'PORT': '3306',

    # }   
  
}

DATABASES["default"] = dj_database_url.parse("postgres://gaurav.singh911805:4QwKmUzRt5LT@ep-jolly-sun-27518314.ap-southeast-1.aws.neon.tech/neondb")

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



SESSION_ENGINE = 'django.contrib.sessions.backends.db'

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/


STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_build', 'static')
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

warnings.filterwarnings("ignore")