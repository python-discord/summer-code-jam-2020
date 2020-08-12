
[![Early Internet Theme Banner](../early_internet_banner.png)](#)
# RSSit
By: Bite-Sized-Bears
## Introduction
We call it the RSSit app. It is a platform to post fun stuff, make virtual communities, and interact (chat) with your community members. We also have added a rss feed for all the content i.e the posts by the users. This helps to generate a rss feed for the users and helpful to integrate in a rss feed reader.


Some features include:

- Create your own community 
- Messaging functionality that allows you to connect and communicate with fellow community members.
- Post and create your very own feed.
- Update your User Profile
- Add Comments to the Posts
- View Top Posts (based on number of  views), Top Communities (based on number of subscribers)
- Obtain a rss feed of the posts from your subscribed communities.
___

### Table of Contents:
- Installation Setup
- References
- License

___
## Installation Setup
Python 3.8 required

(uses postgres database for the setup)


Navigate to root folder
```
cd bite-sized-bears
```

Create and store credentials on .env file 

```
touch .env
nano .env
```

Sample .env file 
```
SECRET_KEY = "put_your_django_secret_key_here"
DB_HOST = "host_link_of_your_postgres"
DB_NAME = "name_of_your_postgres_db"
DB_USER = "userid_your_postgres_db"
DB_PASSWORD = "password_of_your_postgres"
```


### Pipenv Installation

Install pipenv 

```
pip install pipenv
```

Activate environment
```
pipenv shell
```
Install packages (developers should install the dev package)
```
pipenv install 
```

Install dev package (if you are a developer)
```buildoutcfg
pipenv install --dev
```


Check if all packages are installed 
```buildoutcfg
pip list
```

Run development server (windows)
```buildoutcfg
pipenv run server
```
Run development server (Linux)
```buildoutcfg
pipenv run server-l
```


Check lint errors 
```buildoutcfg
pipenv run lint
```

#### Please install a rss feed reader extension for your browser

___
### References
- [Official Django Documentation](https://docs.djangoproject.com/en/3.1/) 
- [Official Docker Documentation](https://docs.docker.com/compose/)
___
### LICENSE

All projects will merged into our Code Jam repository, which uses the [MIT license](../LICENSE). Please make sure that if you add assets, the licenses of those assets are compatible with the MIT license.


Authors: [Ryuga](https://github.com/ryuga-hideki), [Ronit](https://github.com/Ronit-j), [Delta](https://github.com/Ajay-Ratnam)
