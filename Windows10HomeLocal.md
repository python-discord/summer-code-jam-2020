# Windows 10 Home Local Development
Developing on Windows 10 home with out docker.

## Requirements
- You have python, pip and venv installed.
- You have node.js and npm

## Usage

Download the repository and cd into the directory. Then run these commands:
```
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements\windows_local.txt
cd shiny_sheep\frontend\
npm install -G webpack webpack-cli
npm install
npm run dev
cd ..\..
setup_windows_environment.bat
python manage.py migrate
python manage.py runserver
```

You should be able to go to http://127.0.0.1:8000 and see the webapp.
