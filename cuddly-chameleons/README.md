# Cuddly Chameleons
## Team members
- ks129
- Tushavi
- dash-ma

## Important!
This site have to be opened in Safari to work correctly. When using other browsers, you have to log in to see posts because of bug of DRF or DRF Simple JWT. Other browsers append slash to end of URL, but this require authentication at Django side (but it shouldn't). Found this too late, because most of development have been taken place using Safari and we found this bug too late.

## About our project
Our project is simple blog/news site, that implement basic things, like creating, editing, deleting in frontend.

## Setting up and running
### Dependencies
- Docker
- Docker Compose (may come with Docker)
- Python 3.8
- Pipenv
- NodeJS
- NPM

### Django and PostgreSQL
Simplest thing ever (when you have Docker and Docker Compose installed):
```
docker-compose up
```
Django admin is at `localhost:8000/admin` and default admin username is `admin` and password too `admin`

### React
Open new console window. Go to `retro_news` directory, and there run following commands:
```
npm install
```
then, to start:
```
npm start
```
After these steps, you can visit site at `localhost:3000`.
Default superuser (only superusers can create posts) username is `admin` and password too `admin`.

## Using
After logging in as admin, you see button for creating new post in header. When you are in single-post mode and you are admin, you can edit and create posts what is in box. You can see all comments, but for creating new comments, you have to log in. It's impossible to edit or delete comments in frontend (only in backend). New users can register using Sign Up feature. There is also search button in header.
