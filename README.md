# CollaboDev

An open source web application made for collaboration and built on Django.

![Tasks page](https://imgur.com/ahTKDu5)
---

## Installation

 - Clone this repository using 
 ```
 git clone https://github.com/dob9601/CollaboDev.git
 ```
 - Open up a console to the project directory and run the following commands in order to create a superuser and run the server on 127.0.0.1:8000.
 ```
 python manage.py createsuperuser
 python manage.py runserver
 ```
 - If you wish to access the CollaboDev web app from other computers within the same network, run the command (server will be hosted on local machine's ip address):
 ```
 python manage.py runserver 0.0.0.0:80 
 ```
