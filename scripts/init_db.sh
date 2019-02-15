#!/bin/sh
echo "------ Load database tables ------"
python manage.py migrate --noinput

echo "------ create default admin user ------"
echo "from django.contrib.auth.models import User; User.objects.create_superuser('dan.vigliotti', 'dan.vigliotti@webvig.com', 'Changeme')" | python manage.py shell

echo "------ Import initial data ------"
python manage.py loaddata

echo "------ starting gunicorn &nbsp;------"
gunicorn SafeStates.wsgi --workers 2 --log-file -