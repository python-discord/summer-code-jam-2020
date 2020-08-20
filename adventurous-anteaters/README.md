# Code Jam Submission by Team Adventurous Anteaters

- The original ambitious project was to create a "Decentralized Social Network.", something like FidoNet.
- The idea sprouted from the fact that the theme is "Early Internet".
- Back in the day, not everything was on a single central server, and many networks were not even part of the WWW because it was that new. 
- So, we wanted to create something, that would have one or two parent servers, and rest of the servers could be spawned by anyone. 
- Each spawned server would host their own set of Users, and if the servers had access keys to each others, those users would be able to interact with each other as well. 

## However, we are NOWHERE NEAR THAT! So, if someone sees this and wants to try, you have our blessing :) 

#Setup:
1. git clone the project
2. Install Requirements: pip install -r requirements.txt
3. make the migrations: py manage.py makemigrations
                       py manage.py migrate
4. run server: py manage.py runserver


### Flow of the Project: 

- The home page is the profile page, which requires you to be logged in. 
- There's boilerplate check to see if user is logged in, if not, redirect to login page.
- From here, user can register as well if no account is present.
- Once that is done, user will be redirected to Profile page
- Here, he can see the button to "Post a Tweet"
- Clicking on it shows two text boxes, one is the title of the tweet, and the other is the content. 
- Once posted, the user can see all the posted tweets
- There is some small functionality added in the icon bar in header, however, most of it is just for the retro feel. 

### The Following endpoints are active:
- /profile
- /post
- /posted
- /view_tweet
- /register


# What we Learned from participating in the Jam.
- GIT
- HTML/CSS/JS
- Django basics
- Templating (Jinja Templating)
- Team Work
- Time Management (yeah, right!)

[WE EVEN MADE A SHEET](https://docs.google.com/spreadsheets/d/1txXqRkj4V4D4RS1sVEganfGJPK0br0lnWWaH3P1boUM/edit#gid=873896706)



### Credits:
#### The assets came from these MIT licensed repos on Github: 
[Packard Belle: A nostalgic component UI](https://github.com/padraigfl/packard-belle)
[98.css](https://github.com/jdan/98.css)


### Licensing Information

Copyright (c) 2020 @ayushxx7

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
OR OTHER DEALINGS IN THE SOFTWARE.
