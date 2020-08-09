# Project Description
Imagine a world where the internet had arrived centuries early. What would people have used it for back then? 

TeaBay is a website where merchants and civilians from the 1700s can easily and effectively conduct business within an online marketplace. Long-forgotten is the time of passing around flimsy paper ledgers - there's no better way to spend your time and silver than to survey and purchase the exquisite commodities on TeaBay!

# Installation

1. Clone the repository with `git clone https://github.com/fliepeltje/summerjam-private`
2. Install poetry:
   - All platforms, try this first, if it doesn't work use one of the commands below: `python get-poetry -y --preview`
   - Linux: `curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python`
   - macOS (using Python from brew): `pip3 install poetry`
   - Windows (from powershell): `(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python`
3. Reload your shell/terminal
4. `cd` into the project directory from terminal or powershell
5. Run `make verify` to make sure the project is installed correctly. If you see that all tests have passed, then the project is installed.
6. Run `./manage.py runserver` and navigate to `localhost:8000` to make sure you can run the server

## Windows users
I haven't worked with windows in a while, so I would not be able to give very good support for that. If you want your environment to have more resemblance to linux, you could follow this [guide](https://www.laptopmag.com/articles/use-bash-shell-windows-10) - it will allow you to use `bash` on windows and if anything goes wrong in installation I can probably be of more use.

## Loading example data
You can run `./manage.py create_sample_db` to generate a set of randomized data to populate the database. 

You can also run `make reset_db` to flush the database and reload the randomized data.

# Meetings
1. [2020-07-30 - 16:15 UTC + 1 - Agenda](meetings/2020_07_30.md) 