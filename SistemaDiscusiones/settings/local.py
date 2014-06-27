from .base import * 

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'discusiones',
        'USER': 'postgres',                 
        'PASSWORD': 'ricardo',                 
        'HOST': 'localhost',                    
        'PORT': '5432',
    }
}

STATIC_URL = '/static/'
STATICFILES_DIR = [BASE_DIR.child('static')]