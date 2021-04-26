# The Django Blog App
To Begin, we create a directory which would house our project.
navigate into it with your local command line or your inbuilt IDE terminal

This application is built on virtual environment. Pipenv was used.

#### To Install virtual environment using pipenv,
pip install pipenv
next
pipenv install django (to have django installed in the project directory)
pipenv shell (to activate virtual environment)

To create django project
	django-admin startproject myNewDjangoProject

To run first django server
	python manage.py runserver

To create a new django application, from the app folder,
	python manage.py startapp yourappname

#### Note	
- We are not creating login url in our urls.py because it is supplied automatically by django when register 
logic is created
- we've set login_redirect_url on
- Logout is also provided by default
	
This app, is a blog built with the following functionalities:

-    A register page (a new user can register, their details stored in a database file sqlite). 

-    login (checks in the file and logs them in if they are already registered)

-    reset password

-    logout

-    A comment section, which you can only access while logged in.

The project also demonstrates how the .env file is used to hide sensitive data, however, a .env.example file is 
supplied which guides any user without the key.

There's also a requirements.txt file which informs on all the requirements to run the app

this app is hosted on the website 