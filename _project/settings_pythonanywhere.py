"""
Django settings for _project project.

Generated by 'django-admin startproject' using Django 5.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

#git clone https://github.com/VeraSolarova/projekt_pokus  projekt_urazy (nazev slozky do ktere se to ulozi na  pythonanywhere)
#mkvirtualenv --python=python3.10 projekt_urazy_env - vytvori virtualni prostredi ve slozce projekt_urazy_env
#cd projekt_urazy/  - vlezu do slozky kde je projekt
# pip install -r r.txt - nainstaluje knihovny (musim byt ve  slozce projektu)
#git pull -pokud delam nějaky update  na githubu 
#aby se to vubec mohlo zobrazit ALLOWED_HOSTS = ['verasolarova.pythonanywhere.com']
#nastaveni css  - v projektu  upravim cesty v settings. 
#STATIC_URL = 's/'
#staticke dela vyvojar, dynamicke -MEDIA - treba obrazky doda uzivatel¨
#STATIC_ROOT = 'static/'
# na  https://www.pythonanywhere.com/ v zalozce web nastavim cestu
#/s/	/home/verasolarova/projekt_urazy/static	 
# python manage.py collectstatic  - na pythonanywhere.com v konzoli bash
#  Debug = false , secret key = nebude zverejnen  - pres sytemove  promenne - napr v jason nebo ve specialnoim souboru
#databazove nastaveni - password - take musi byt schovane - ostra databaze s uzivateli se musi prejmenovat, aby se nprepsala pres github db sql lite  3 pro vyvoj, - pro ostry provoz postgre, php databze 


# settings pro web nastavím na pythonanywhere.com - web , WSGI configuration file:/var/www/verasolarova_pythonanywhere_com_wsgi.py

# +++++++++++ DJANGO +++++++++++
# To use your own django app use code like this:
#import os
#import sys
#
## assuming your django settings file is at '/home/verasolarova/mysite/mysite/settings.py'
## and your manage.py is is at '/home/verasolarova/mysite/manage.py'
#path = '/home/verasolarova/projekt_urazy'
#if path not in sys.path:
   # sys.path.append(path)
#
#os.environ['DJANGO_SETTINGS_MODULE'] = '_project.settings_pythonanywhere'
#
## then:
#from django.core.wsgi import get_wsgi_application
#application = get_wsgi_application()




from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-yz#jvw56^nz8a^*+z3ru1az@5r6q=$-%2rx*aiutg5f+281^bb'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['verasolarova.pythonanywhere.com']

INTERNAL_IPS = ["127.0.0.1"]
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles', 
    'debug_toolbar',
    'urazy',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = '_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],  # Přidání vlastního adresáře šablon
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'urazy.context_processors.kategorie_context',  # Přidání vlastního procesoru
            ],
        },
    },
]






WSGI_APPLICATION = '_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'verasolarova$default',
        #nazev databaze z pythonanywhere.com
        'USER': 'verasolarova',
        #username z  pythonanywhere.com
        'PASSWORD':'hesloheslo',
        #heslo nastavene k databazi z pythonanywhere.com
        'HOST':'verasolarova.mysql.pythonanywhere-services.com',
        #Database host address: z pythonanywhere.com
        'PORT':'3066',
        #port na mysql 
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 's/'
#staticke dela vyvojar, dynamicke -MEDIA - treba obrazky doda uzivatel¨
STATIC_ROOT = 'static/'
# na  https://www.pythonanywhere.com/ v zalozce web nastavim cestu
#/s/	/home/verasolarova/projekt_urazy/static	 
# python manage.py collectstatic  - na pythonanywhere.com v konzoli bash
#  
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / "_media" #kam  se bude ukladat 

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'