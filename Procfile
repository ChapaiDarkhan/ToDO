release: python manage.py migrate

web: gunicorn news.wsgi

worker: python tasks.py