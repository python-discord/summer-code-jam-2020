#  Concerned Coyotes

### Project overview

Our project is an app for early risers. It's meant to provide information for users, who get up early which includes news, a to-do list for the day, a weather forecast and interesting wikipedia articles.

In order to provide individual information, a login is required.

###  Setup

In order to setup you need to run
```
pip install -r requirements.txt
```

in a Python 3.8 environment.

Switch to the project directory

```
cd earlyinternet
```

Setup the project itself

```
python manage.py migrate
python manage.py setup_tasks
python manage.py run_tasks
```

### Run the application

To run the application use

```
python manage.py runserver
```

and check it out with your favorite browser.

### Missing features

Unfortunately we didn't have enough time to include all our planned features. The one's that didn't make it are


* Breakfest recipes
* calender integration

### References

The background image was taken from [unsplash](https://unsplash.com/photos/IKbpXrInCJY)

Icons were provided by [tablericons](https://tablericons.com/) 


