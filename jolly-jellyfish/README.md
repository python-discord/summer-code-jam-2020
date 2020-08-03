# Jolly Jellyfish
![Jolly Jellyfish logo](team_logo.svg)

In today's fast moving society, you may want to have your own web property along the information superhighway... 
However, with the latest shutdown of Yahoo!'s Geocities, where to? Don't worry! Halfway™️ has got your back.
Initially named as a joke on Medium, we've expanded into a profitable enterprise.
However, our angel investors did not quite believe us and left us for the next Google...
Now that we're bankrupt, we have a cultural obligation to opensource this.

## Idea

An old-internet style site-creation tool that comes with the kitchen sink.

Simply put, users can choose from a variety of templates and customize it any-which-way.
After this, they can take their site to the forum to get ~~likes~~ feedback.
The most liked sites appear on the front page, along with the most liked users and most recent sites.

## Initial Setup
### wkhtmltoimage
In order to generate page thumbnails wkhtmltoimage.exe is required for python package `imgkit`.
Download from [https://wkhtmltopdf.org/downloads.html][1] and set the system environment variable **WKHTML_TO_IMAGE** to the executable's path.

E.g. On Windows (admin) with a .exe file, this is done with:
```batch
...\> setx WKHTML_TO_IMAGE D:\Path\to\wkhtmltox\bin\wkhtmltoimage.exe /m
```
(Use `SETENV` command on UNIX)

In a production environment, this process would obviously not be needed as the server would be running a known OS.
Therefore, only one executable would need to be download to the src directory and then hard linked within the code, rather than having to use `os.environ`.

### pipenv
```shell script
$ pipenv install
$ pipenv shell
(venv) $ python manage.py makemigrations  # TODO: this might be optional.
(venv) $ python manage.py migrate
```

## Usage
```shell script
(venv) $ python manage.py runserver
```

[1]: https://wkhtmltopdf.org/downloads.html
