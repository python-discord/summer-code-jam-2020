# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim-buster

EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

# Install pip requirements
RUN python -m pip install --upgrade pip
ADD requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app/spacebook
ADD . /app

# Switching to a non-root user, please refer to https://aka.ms/vscode-docker-python-user-rights
RUN useradd appuser && chown -R appuser /app
USER appuser

# Collect static files
RUN cd spacebook
RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py loaddata db.json
RUN python manage.py collectstatic --noinput
RUN cd ..

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
# File wsgi.py was not found in subfolder:mysterious-mice. Please enter the Python path to wsgi file.
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "spacebook.wsgi"]
