#!/bin/bash

NAME='web-app'
DJANGODIR=$APP_FOLDER/DjDevOps
NUM_WORKERS=3
DJANGO_SETTINGS_MODULE=DjDevOps.settings
DJANGO_WSGI_MODULE=DjDevOps.wsgi

echo 'Starting…'

cd $DJANGODIR
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

echo "Waiting for db initialization..."
python manage.py check --database default
until [ $? -eq 0 ];
do
  sleep 2
  python manage.py check --database default
done
echo "Connected!"

python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py loaddata ./users/fixtures/users_data.json

exec /usr/local/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
	--name $NAME \
	--workers $NUM_WORKERS \
	--bind '0.0.0.0:8000' \
	--timeout 1000 \
	--log-level=debug \
	--log-file=- 

