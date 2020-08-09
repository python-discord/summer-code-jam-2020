# Lonely Lemmings

Our team created a Django-based feed/board web application for creating and posting your own GIF images. Users can
create their own GIF images frame by frame with a paint-like tool and save them in a project. Projects can be shared by 
users and seen on the main project feed. Basic account, authentication, and login functionality has been added using 
Django's built-in authentication packages.

## Team

- Pectacius
- BatmanBoxers xotwod
- shawkagawa
- BrayaON
- Jordo

## Application Installation Requirements

The following items are required to install this application:
- Python 3.8
- Pipenv

## Application Setup

1. Change into the `lonely-lemmings/earlyinternet` directory

2. Run `pipenv sync` to install the project's dependencies into a new environment

3. Run `python manage.py runserver` to run the application development server and open it in your browser

## Gif App Usage

1. Log in with the following user credentials, or create your own user:
   - Username:   Password: 
2. On the top right-hand side, click "New Project" and enter a name for the new project. Click "OK"
3. On the next page, you're presented with a canvas and a set of tools. You can draw each frame of your GIF here. You
can advance to the next frame by hitting next.
4. When you are done drawing, click the "View" button to preview your creation, and then click "Save to Server".

