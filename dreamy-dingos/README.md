# Dreamy Dingos

## Chat Rooms

When we thought about the Early Internet, we remembered chat rooms, which were popular some 20 years ago. <br>
So we've tried to create a similar chat rooms application, where you log in, select a room based on a topic you're interested in and chat with people online.

Unfortunately, we had to work with limited resources since two people in our team haven't had power since Tuesday due to a storm on the US east coast. Availability of other team members was also somewhat limited during the week, and even though we got some input from each member, we managed to implement only a fraction of planned features. For instance, frontend is non-existent unfortunately.

## Built with

- [Django](https://github.com/django/django)
- [Django Channels](https://github.com/django/channels)
- [Docker](https://github.com/docker)

## How to install

The project uses Docker as a build tool, so running the project is as simple as:

```
docker-compose run web python manage.py makemigrations && \
docker-compose run web python manage.py migrate && \
docker-compose up -d
```

## How to use

As mentioned in the beginning, only a part of intended functionality was implemented, so user management is unfortunately not used. By default the application runs on port 8000. To try out the existing functionality go to: 

```
http://localhost:8000/
```

There you can click the "View rooms" button to see existing chat rooms or create a new one.

After you've joined a room, try sending a message in a chat window. After that, open the same link in a new browser tab and you should see that message and you can also send a new one. 