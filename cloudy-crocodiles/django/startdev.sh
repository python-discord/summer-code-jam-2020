echo Waiting for DB
python pgwait.py
echo Applying migrations
python manage.py migrate
echo Starting development server
python manage.py runserver 0.0.0.0:8000