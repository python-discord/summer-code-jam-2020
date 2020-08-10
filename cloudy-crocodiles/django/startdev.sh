echo Waiting for DB
python pgwait.py
echo Applying migrations
python manage.py migrate
if [ "$LOAD_FIXTURES" == "True" ];
then
  echo Loading Fixtures
  python manage.py loadfixtures
fi
echo Starting development server
python manage.py runserver 0.0.0.0:8000