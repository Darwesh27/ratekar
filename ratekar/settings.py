"""
Django settings for ratekar project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

from local_settings import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!


# DEBUG = True if os.environ['DEBUG'] == 'dev' else False

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['localhost', '130.211.243.115']

# Custome user model
AUTH_USER_MODEL = "social.User"

# from .backends import CustomAuth
# AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend', CustomAuth)

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'personality',
	'social',
	'timeline',
	'api',
	'web',
	# 'south', 
	'rest_framework',
	'pipeline',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'ratekar.urls'

WSGI_APPLICATION = 'ratekar.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': DB_NAME, 
		'USER': 'root',
		'PASSWORD': DB_PWD,
		'HOST' : DB_HOST,
		'PORT': '3306',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_URL = "/static/media/"

MEDIA_ROOT = os.path.join(BASE_DIR,'static', 'media')


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATICFILES_DIRS = (
	os.path.join(BASE_DIR, 'api/static'),
)

STATIC_ROOT = os.path.join(BASE_DIR, 'static', 'static_final')

STATIC_URL = '/static/'

STATIC_PATH = os.path.join(BASE_DIR, 'api','static')


# pipeline settings 
STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'

PIPELINE_CSS = {
    'core': {
        'source_filenames' : (
            'bower_components/angular-material/themes/green-theme.css',
            'bower_components/angular-material/themes/red-theme.css',
            'css/*.css',
            'js/app/*/*.css',
            'js/app/*/*/*.css',
            'js/app/*/*/*/*.css',
            'js/app/*/*/*/*/*.css',
        ),
        'output_filename': 'css/main.css',
    }
}

PIPELINE_JS = {
    'check': {
        'source_filenames': (
            'js/app/components/toolbar/toolbar-module.js',
            'js/app/components/toolbar/notifications/toolbar-notifications-module.js',
            'js/app/components/stream/post/post-module.js',
            'js/app/components/stream/stream-module.js',
            'js/app/components/profile/profile-module.js',
            'js/app/components/backend/backend-module.js',
            'js/app/components/right-pane/right-pane-module.js',
            'js/app/components/auth/auth-module.js',
            'js/app/components/welcome/welcome-module.js',
            'js/app/helpers/dropdown/dropdown-module.js',
            'js/app/*/*.js',
            'js/app/*/*/*.js',
            'js/app/*/*/*/*.js',
            'js/app/*/*/*/*/*.js',
            'js/app/app.js',
        ),
        'output_filename': 'js/check.js',
    }
}


PIPELINE_MIMETYPES = (
  (b'text/coffeescript', '.coffee'),
  (b'text/less', '.less'),
  (b'text/javascript', '.js'),
  (b'text/x-sass', '.sass'),
  (b'text/x-scss', '.scss')
)


# logging 

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/mylog.log'),
            'maxBytes': 1024*1024*5, # 5 MB
            'backupCount': 5,
            'formatter':'standard',
        },  
        'request_handler': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/django_request.log'),
            'maxBytes': 1024*1024*5, # 5 MB
            'backupCount': 5,
            'formatter':'standard',
        },
        'db_handler': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/django_db.log'),
            'maxBytes': 1024*1024*5, # 5 MB
            'backupCount': 5,
            'formatter':'standard',
        },
    },
    'loggers': {
        '': {
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': True
        },
        'django.request': {
            'handlers': ['request_handler'],
            'level': 'DEBUG',
            'propagate': False
        },
		'django.db': {
			'handlers': ['db_handler'],
			'level': 'DEBUG',
			'propagate': False
		},
    }
}


