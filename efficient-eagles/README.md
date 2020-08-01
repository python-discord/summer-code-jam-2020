# Efficient Eagles

## How to set-up
Create web-variables.env file in the efficient-eagles/early_internet/ directory:
```
POSTGRES_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
```

Build containers:

> docker-compose build

Apply migrations:

> docker-compose run web python manage.py migrate 

## How to run 
> docker-compose up
