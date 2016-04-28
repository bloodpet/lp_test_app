# Unsubscribe Test App

## Synopsis
This project shows how to use the included unsubscribe django app.


## Download
```
git clone git@github.com:bloodpet/lp_test_app.git project_name
cd project_name
```


## Installation
You could choose to install this using docker-compose or manually


### Docker Installation
This will automatically install all the requirements

#### 1. Settings
Copy *test_app/local_settings.py.docker* to *test_app/local_settings.py*.
`cp test_app/local_settings.py.docker test_app/local_settings.py`

#### 2. Database
Create DB tables
`docker-compose run --rm web ./manage.py migrate`


### Local Installation
This would install the requirements to your local system

#### 1. Settings
Copy *test_app/local_settings.py.dist* to *test_app/local_settings.py* and edit accordingly. You probably need to change the database settings

#### 2. Requirements
`pip install requirements.txt`

#### 3. Database
`./manage.py migrate`


## Run

### On docker
`docker-compose start`

### On local
`./manage.py runserver`


## Tests

### On docker
docker-compose run --rm web ./manage.py test

### On local
./manage.py test
