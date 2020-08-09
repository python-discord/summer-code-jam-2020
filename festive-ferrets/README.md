# MyFirstWebsite by Team Festive-Ferrets

![test-frontend](https://github.com/jannisko/summer-code-jam-2020/workflows/test-frontend/badge.svg)
![test-django](https://github.com/jannisko/summer-code-jam-2020/workflows/test-django/badge.svg)
![.github/workflows/lint.yml](https://github.com/jannisko/summer-code-jam-2020/workflows/.github/workflows/lint.yml/badge.svg)

Have you ever wondered what it was like to be one of the first web-developers ever?
When you could count all competitors in your field on one hand?
What would you have created in this situation?
A buggy message board and an unfinished game of tictactoe? **Exactly**!

Visit the live version of our site [here](code-jam-2020.jannisk.de).

## Motivation

This project was created for the [Python Discord Summer Code Jam 2020](https://pythondiscord.com/pages/code-jams/code-jam-7/) in August 2020.
The goal was to develop a Django-based web application with the theme "Early Internet".
You can find the main repository of the code jam [here](https://github.com/python-discord/summer-code-jam-2020).

<img src='images/summer_cj_2020_banner.png' width=600 class="center">


## Getting Started

```bash
git clone git@github.com:jannisko/summer-code-jam-2020.git
cd summer-code-jam-2020/festive-ferrets/
```

### Backend

The backend for this project was written in Python 3.8, using Django 3 as a framework.

First install all necessary Python packages:
```bash
pip install -r requirements.txt
```

By default the Django will use the config file ```backend/dev.env```.
You can change some of the behavior there.

Run all tests:
```bash
python backend/manage.py migrate
python backend/manage.py test
```

Then run the development server on port 80 using:
```bash
python backend/manage.py runserver 0.0.0.0:80
```


### Frontend

The frontend was created using node.js 14 and Angular.

First install the the dependencies:
```bash
cd frontend/code-jam
npm install
```

Then start the development server on port 4200 using:
```bash
npm start
```

## Deployment

To deploy using Docker first rename ```db.env.example``` to ```db.env.prod``` and ```django.env.example``` to ```django.env.prod```.
You should also change these files to suit your needs.

To then start all services type:
```bash
docker-compose up -d
```


## Team Members

- [AmazAkar](https://github.com/AmazAkar) - Backend development
- [AnixDrone](https://github.com/AnixDrone) - Backend & Frontend development
- [jannis](https://github.com/jannisko) - Backend development & DevOps
- [martinkozle](https://github.com/martinkozle) - Backend & Frontend development
- [VerheeckeLorenzo](https://github.com/VerheeckeLorenzo) - Backend development



## License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details