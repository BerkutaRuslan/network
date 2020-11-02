##General info
Network Project

## Docs
https://documenter.getpostman.com/view/7360798/TVYM4b2Q


## How to run a project
Activate virtualenv: (venv - your virtual environment name)

$ source venv/bin/activate
To start server got to the project root and run:

$ python3 manage.py runserver
To make and apply migrations run the following command:

$ python3 manage.py makemigrations
$ python3 manage.py migrate
$ python3 manage.py loaddata user_data.json
$ python3 manage.py loaddata post_like_data.json