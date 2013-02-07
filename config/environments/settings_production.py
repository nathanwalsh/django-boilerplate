from settings_common import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOW_ROBOTS = True

DATABASES = {
    'default': {
        'ENGINE'    : 'django.db.backends.mysql',
        'NAME'      : '',
        'USER'      : '',
        'PASSWORD'  : '',
        'HOST'      : '127.0.0.1',
        'PORT'      : '',
    }
}