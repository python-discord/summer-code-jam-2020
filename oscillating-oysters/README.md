# Oscillating Oysters

### Woohoo! Let's go!!!

# instructions:

Right now, if you have Docker installed locally you can just use docker-compose:
```
docker-compose up -d
```

Run migrations, setup a super user
```
docker-compose run --rm web python manage.py migrate
docker-compose run --rm web python manage.py createsuperuser
```

And the app should be running on localhost:8000 (or whatever ip docker is setup for)

---
> ps: if you want to test the multiuser chat just make a new user (go to /admin) and log them in in an incognito window

---

To load some test data (located in MUD/fixtures) including a useri(name:oyster, pwd:oysteroyster
```
docker-compose run --rm web python manage.py loaddata test_data.json
```
