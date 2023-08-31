from . import *
from .base import *


ALLOWED_HOSTS = ["*"]
SECRET_KEY=env('PRODUCTION_SECRET_KEY')
DEBUG=False

DATABASES = {
	'default': {
			'ENGINE': 'django.db.backends.postgresql',
			'NAME' : os.getenv('POSTGRES_DB'),
			'USER': os.getenv('POSTGRES_USER'),
			'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
			'HOST': os.getenv('DATABASE_PROD_HOST'),
			'PORT': '5432',
        	'ATOMIC_REQUESTS': True
	}
}

