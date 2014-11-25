"""
Django settings for ratekar project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6=$a&uh7q+j=4b#4)n3c3yfylz5ri5*mb5-3!=qq9k^$j9%@_u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['localhost']

# Custome user model
AUTH_USER_MODEL = "social.User"

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
	'south', 
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
        'NAME': 'ratekar',
		'USER': 'root',
		'PASSWORD': 'root',
		'HOST' : 'localhost',
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


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATICFILES_DIRS = (
	os.path.join(BASE_DIR, 'api/static'),
)

STATIC_ROOT = os.path.join(BASE_DIR, 'api/static_final/')

STATIC_URL = '/static/'

STATIC_PATH = os.path.join(BASE_DIR, 'api/static/')


# pipeline settings 
STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'
PIPELINE_JS = {
    'check': {
        'source_filenames': (
            'bower_components/jquery/dist/jquery.min.js',
            'js/jquery.wookmark.js',
            'bower_components/angular/angular.min.js',
            'bower_components/angular-animate/angular-animate.min.js',
            'bower_components/angular-route/angular-route.min.js',
            'bower_components/angular-aria/angular-aria.min.js',
            'bower_components/angular-cookies/angular-cookies.min.js',
            'bower_components/hammerjs/hammer.min.js',
            'bower_components/angular-material/angular-material.min.js',
            'bower_components/angular-loading-bar/src/loading-bar.js',
            'bower_components/angular-ui-router/release/angular-ui-router.min.js',
            'bower_components/angular-elastic/elastic.js',
            'js/app/components/toolbar/toolbar-module.js',
            'js/app/components/toolbar/notifications/toolbar-notifications-module.js',
            'js/app/components/stream/post/post-module.js',
            'js/app/components/stream/stream-module.js',
            'js/app/components/profile/profile-module.js',
            'js/app/components/backend/backend-module.js',
            'js/app/components/right-pane/right-pane-module.js',
            'js/app/helpers/dropdown-module.js',
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


