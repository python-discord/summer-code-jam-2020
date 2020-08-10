# Rubbery Raccoons - Wired.com
### Overview
The Rubbery Raccoons present wired.com circa 1995 recreated in Django. Wired.com was the online presence of the popular Wired magazine. This was one of the first publications to create an online presence coming online in 1993. Interstingly, Wired magazine and Wired.com split in the late 1990s before being reunited in 2006. The two now remain very close editorially again. Wired was a pioneer of providing news in a digital age and their successful news website eventually evolved into multiple international spinoffs, a search engine, a blog and even their own stock index.

### Getting Started
Our submission is written entirely in Django with a sqlite DB for development. All you'll need is a Django 3+, python 3.7+ environment. Some sample getting started steps:
1. `pip install Django`
1. `cd rubbery-raccoons/wired`
1. `python manage.py migrate`
1. `python manage.py loaddata fixtures/dummy_data.json`
1. `python manage.py runserver`

### Functionality
The first thing you'll want to do is of course create a user account, so click on register on the left nav. Since this website is circa mid-90's any simple 8 character password will do. Using the shortest password you can think of and then reuse across all your other accounts is encouraged to be period-accurate. After you create a user, go ahead and login with your new super secure credentials.

You'll now have a new link in your left nav, `Author Tools`, go ahead and click on that to view your created content. Feel free to click on `Compose a new article` and begin populating the site with your own content! You can always go back to the homepage and check out how the site is looking.

Finally, feel free to test out our search functionality on the homepage.
