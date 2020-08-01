![Proud Puffins](images/Proud_Puffin_banner.png)
# Proud Puffins

This is the default README of your team's project. Please replace this by a README with more information on your project. At the very least, your README should contain information on how to set-up and run your project.

We be Puffins, and we be proud!
* ergomacros
* ImaMoonky
* PDXCardinal78
* XPOjabar
* rr


## Dev stuff

### [Populating profiles database](https://docs.djangoproject.com/en/3.0/howto/initial-data/)
- Add new entries into `earlydating/fixtures/profiles.json`
- Run migrations to setup Profile database
- Run ```python3 manage.py loaddata profiles.json```
- Run server :)


### Code organisation

- Dev dependencies go in `requirements-dev.txt`
- Normal dependencies go in `requirements.txt`

### Setting up your repo

Clone this repo:

```bash
$ git clone https://github.com/babarrett/summer-code-jam-2020.git
```

Create a virtualenv:

```bash
$ python3.8 -m venv <name_of_virtualenv>
```

Activate it:

```bash
$ . <name_of_virtualenv>/env/activate
```

Install dependencies

```bash
(env) $ cd ./summer-code-jam-2020/proud-puffins/ # navigate to our folder
(env) $ pip install -r requirements.txt # install normal requirements
(env) $ pip install -r requirements-dev.txt # install dev as well
```

Set up pre-commit hooks

```bash
(env) $ cd ..
(env) $ pre-commit --version # make sure this outputs something
(env) $ pre-commit install 
```

Now it should run before your commit :) 



## [MIT license](../LICENSE)

## [Credits and sources](Credits%20and%20sources.md)

