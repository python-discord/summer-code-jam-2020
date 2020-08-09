# FORUMTHING

Our site is basically just a forum with an auth system using Discord. People can create threads, post messages on said threads, and also edit/delete their messages. Threads are divided into three topics currently: General, Coding (well, this _is_ a code jam), and Jokes.

## Running Directions

1. Set your current working directory to .../summer-code-jam-2020/observant-otters/forumthing.
2. Run `python manage.py runserver`.
3. That's all!


## Environement Variables

- `DISCORD_CLIENT_ID`: The Discord Client ID of the app to use for OAuth2.
- `DISCORD_CLIENT_SECRET`: The Discord Client Secret of the app to use for OAuth2.
- `SECRET_KEY`: The secret key for our Django site.

## Build

`docker-compose up`
=======

