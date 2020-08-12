# Use base 3.7 image
FROM python:3.7-buster

# Make an "/app/" directory and make it the working dir
RUN mkdir /app

# Add all project files to an "/app/" directory
COPY . /app/

# Change to app folder 
WORKDIR /app

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r ./requirements.txt
RUN pipenv install --skip-lock
RUN pipenv run python3 ./manage.py makemigrations 
RUN pipenv run python3 ./manage.py migrate
RUN pipenv run python3 ./manage.py generatepages Memes,INFO Pencil,BIZ Tigers,BLOG

# Go into the pipenv shell and run the code
CMD pipenv run python3 ./manage.py runserver 0.0.0.0:8000