# Funky Flamingos

## Setup

###

### Requirements

- Python 3.8+

###

### Installation

Install the dependencies/packages

```python
pip install -r requirements.txt
```

Go to the project folder
```python
cd rinky_dink
```
###

### Usage Instructions

```python
# Make Migrations First
python manage.py migrate
```


```python
# Run server
python manage.py runserver

Project will run on:
http://localhost:8000
```
# Current Features!
  - Upload a file to http://localhost:8000/file/upload
  - Checks if the file with the same name was previously uploaded if the file with the same name is there then calculates the hash value of both the files and discards the file to save on the server if the hash value matches. If the hash value has been changed then save that file with the new name.
  - Checks changes made to uploaded file if file with the same name was previously uploaded

##
