# Python Flask read MySQL DB example

The app presumes MySQL database `test` with table `users` (id, name) and MySQL user `user`.

## Install

MySQL needs to be installed.

`pip install mysqlclient`

`apt install libmysqlclient-dev`

`pip install -r requirements.txt`

## Environment variables

`$ export DB_PWD=password` where password is mysql password for user to test database.


## Run

`python3 main.py`

Go to 

- see all users
[localhost:5000/users](localhost:5000/users)

- see user with e.g. id 1
[localhost:5000/users/1](localhost:5000/users/1)
