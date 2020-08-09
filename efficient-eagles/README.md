# Efficient Eagles
## How to set-up
Build containers:

> docker-compose build

Apply migrations:

> docker-compose run web python manage.py migrate 

Load fixtures:

> docker-compose run web python manage.py loaddata data.json

## How to run 
> docker-compose up
