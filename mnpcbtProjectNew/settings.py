"""
Django settings for mnpcbtProjectNew project.

Generated by 'django-admin startproject' using Django 3.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'y0-uv=knym2el10@)t*km+(ehdc!=#9jfk&(qu-6$a#*2&n&nm'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'mnpcbt-new.ru', 'www.mnpcbt-new.ru']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'corsheaders',
    'ckeditor',
    'ckeditor_uploader',
    'sitetree',
    'mptt',
    'import_export',
    'main.apps.MainConfig',
    'news.apps.NewsConfig',
    'articles.apps.ArticlesConfig',
    'structure.apps.StructureConfig',
    'reviews.apps.ReviewsConfig',
    'implink.apps.ImplinkConfig',
    'moscowDoctor.apps.MoscowdoctorConfig',
    'management.apps.ManagementConfig',
    'regularPages.apps.RegularpagesConfig',
    'needToKnow.apps.NeedtoknowConfig',
    'videoclips.apps.VideoclipsConfig',
    'services.apps.ServicesConfig',
    'schoolNurses.apps.SchoolnursesConfig',
    'mnpcbtMain.apps.MnpcbtmainConfig',
    'schoolPatient.apps.SchoolpatientConfig',
    'smi.apps.SmiConfig',
    'search.apps.SearchConfig',
    'employees.apps.EmployeesConfig',
    'covidSpecialists.apps.CovidspecialistsConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.BrokenLinkEmailsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True

CORS_ORIGIN_WHITELIST = [
    'http://127.0.0.1:8000',
    'https://mdbootstrap.com',
]


ROOT_URLCONF = 'mnpcbtProjectNew.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'mnpcbtProjectNew.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'u1235053_default',
        'USER': 'u1235053_default',
        'PASSWORD': 'N!ACo97k',
        'HOST': '37.140.192.57',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'static_collections')
STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [STATIC_DIR, ]
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
CKEDITOR_UPLOAD_PATH = "uploads/"


CKEDITOR_CONFIGS = {
    "default": {
        "removePlugins": "stylesheetparser",
        'allowedContent': True,
        'toolbar_Full': [
        ['Styles', 'Format', 'Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat' ],
        ['Image', 'Flash', 'Table', 'HorizontalRule'],
        ['TextColor', 'BGColor'],
        ['Smiley','sourcearea', 'SpecialChar'],
        [ 'Link', 'Unlink', 'Anchor' ],
        [ 'NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl', 'Language' ],
        [ 'Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates' ],
        [ 'Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo' ],
        [ 'Find', 'Replace', '-', 'SelectAll', '-', 'Scayt' ],
        [ 'Maximize', 'ShowBlocks' ]
    ],
    }
}

SITE_ID = 1
