# DjangoCities (Cloudy Crocodiles)

`GeoCities` was an old service that allowed users to create web pages and link them to a `city`. These cities could have thousands of websites linked to them.

So, to bring back the nostalgia of working with `HTML2` and creating websites that would live on the internet for everyone to see with, we created `DjangoCities`. But wait, there's a twist. `DjangoCities` comes with a modern frontend. So you won't have to wait for a page reload after every click.

Sources:

- [Web Archive](https://web.archive.org/web/19961219233921/http://www.geocities.com/homestead/homedir.html)
- [GeoCities Gallery](https://geocities.restorativland.org/)

## Features

- Login/Register
- An overview of all the cities
- A sitemap of every city
- Allow user to create their own sites with `HTML1` or `HTML2`
- A custom HTML parser to filter out valid `HTML1` and `HTML2`

## Technology/Frameworks used

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [GraphQL](https://graphql.org/)
- [Ariadne](https://ariadnegraphql.org/)
- [Postgres](https://www.postgresql.org/)
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [Vue](https://vuejs.org/)
- [Quasar](https://quasar.dev/)
- [Docker](https://www.docker.com/)

## Pre-requisites

- Docker
- docker-compose

## Running in development mode

There are two ways to run this app. One is standard, the other loads fixtures prior to startup.

### Standard way

```bash
$ docker-compose -f docker-compose.dev.yml up
```

### Load Fixtures

**DANGER ZONE** - This can cause data loss, and should only be run before you run this project for the first time (or if you do not care about changes you made to the database).

You can load fixtures prior to startup by setting the environment variable `LOAD_FIXTURES=True`. On a Linux system, you can do so by executing the following command:

```bash
$ LOAD_FIXTURES=True docker-compose -f docker-compose.dev.yml up
```

You can also set it directly in `docker-compose.dev.yml`.

> Frontend will be served on [http://localhost:8080](http://localhost:8080)

> You should now be able to connect to Django at [http://localhost:1234](http://localhost:1234). Additionally, you can access the Django administration interface at [http://localhost:1234/admin/](http://localhost:1234/admin/) With user `admin` and password `admin`, provided that you have loaded the fixtures, and play with the `graphiql` interface at [http://localhost:1234/graphql/](http://localhost:1234/graphql/).

Press `ctrl-c` to kill the servers.
