from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'admin',
        'PASSWORD': 'sua_senha',
        'HOST': 'seu-endpoint-rds',
        'PORT': '5432',
    }
}