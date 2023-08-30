from . import *
from .base import *


ALLOWED_HOSTS = ["*"]
SECRET_KEY=env('PRODUCTION_SECRET_KEY')
DEBUG=False


DATABASES = {
	'default': {
			'ENGINE':'django.db.backends.postgresql',
			'NAME' : env('POSTGRES_DB'),
			'USER': env('POSTGRES_USER'),
			'PASSWORD': env('POSTGRES_PASSWORD'),
			'HOST': env('DATABASE_PROD_HOST'),
			'PORT': '5432',
            'ATOMIC_REQUESTS': True
	}
}

