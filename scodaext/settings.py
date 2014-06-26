"""
Django settings for scodaquiz project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SITE_ID = 1


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get(
    'SECRET_KEY',
    '9j457p@^$@)7fh+z4!3l^w5!b_$#nc#cxtu7$_a_jfwwf6-+v&'
    )

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', 'true') == 'true'

TEMPLATE_DEBUG = DEBUG


# Application definition

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'reversion',
    'djangocms_text_ckeditor',
    'cms',  
    'mptt',  
    'menus',  
    'sekizai',  
    'djangocms_admin_style',  
    'django.contrib.admin',
    'django.contrib.messages',  
    'hvad',
    'south',
    'taggit',
    'scodaext.apps.badgeclient',
    'scodaext.apps.simplequiz',
    'scodaext.apps.feedbackform',
    'scodaext.apps.courses',
    'scodaext.apps.users',
    'scodaext.apps.mdplugin',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',  
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'scodaext.urls'

WSGI_APPLICATION = 'scodaext.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

import dj_database_url
DATABASES = {}
DATABASES['default'] = dj_database_url.config()
ECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
ALLOWED_HOSTS = ['*']

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES=[
    ('en','English'),
    ('es','Spanish'),
    ('fr','French'),
    ('pt','Portuguese'),
    ]
    
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'scodaext', 'templates'),
    )

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    )

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'cms.context_processors.cms_settings',
    'sekizai.context_processors.sekizai',
)
STATIC_ROOT = 'staticfiles'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'scodaext', 'static'),
    )
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder"
    )

CMS_TEMPLATES = (
    ('template_1.html', 'Basic Page'),
    ('frontpage.html', 'Frontpage'),
)

LOGIN_URL = "/user/login/"

SOUTH_MIGRATION_MODULES = {
    'taggit': 'taggit.south_migrations',
    }
