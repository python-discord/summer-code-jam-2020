# FORUMTHING

Our site is basically just a forum with a simple auth system. People (when logged in) can create threads, post messages on said threads, and also edit/delete their messages. Threads are divided into three topics currently: General, Coding (well, this _is_ a code jam), and Jokes.

## Running Directions (Without Docker)

1. Set your current working directory to .../summer-code-jam-2020/observant-otters.
2. Install dependencies with `pip install -r requirements.txt`.
3. Switch your cwd to .../summer-code-jam-2020/observant-otters/forumthing.
3. Run `python manage.py runserver`.
4. That's all!


## Environement Variables

- `SECRET_KEY`: The secret key for our Django site.

## Build

`docker-compose up`
=======

