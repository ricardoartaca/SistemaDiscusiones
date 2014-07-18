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
STATICFILES_DIRS = [BASE_DIR.child('static')]

SOCIAL_AUTH_FACEBOOK_KEY = '306057166223037'
SOCIAL_AUTH_FACEBOOK_SECRET = '0dc74235ded88b3ccfbad5fd8b93f525'

SOCIAL_AUTH_TWITTER_KEY = 'R5PQxOReXJi5caczcpPXeNb76'
SOCIAL_AUTH_TWITTER_SECRET = 'XJzXlo6zJLgHTpgIYmwbLLkVxlHSZQloNyEK4RKnRcCkdCH3Z6'

