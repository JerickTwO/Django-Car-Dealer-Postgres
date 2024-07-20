web: python manage.py collectstatic --noinput && gunicorn dealer_project.wsgi --workers 3 --bind 0.0.0.0:$PORT --log-file - --log-level debug
