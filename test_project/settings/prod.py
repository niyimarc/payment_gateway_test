from .base import *

DEBUG = False
ALLOWED_HOSTS = []

# this is the path to the static folder where css, js and images are stored
STATIC_DIR = BASE_DIR / 'static'
# path to the media folder 
MEDIA_ROOT = BASE_DIR / 'media'

STATIC_URL = 'static/'
MEDIA_URL = 'media/'

STATICFILES_DIRS = [
    STATIC_DIR,
]