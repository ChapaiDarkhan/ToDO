# TODO
Create and update task information

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.
```bash
pip install -r requirements.txt
```

## Usage

For run this project:
```bash
./manage.py runserver
```

For run with docker-compose:
```bash
docker-compose up --build
```

###Admin
Admin page accessible by this URL: "http://127.0.0.1:8000/admin"

Admin page you can manage of the web-site.

###API

API page accessible by this URL Local: "http://127.0.0.1:8000/api"

In api page you can create, delete and update all the data

For register user with sending password to email:
http://localhost:8000/api/rest-auth/registration/

For logout from app:
http://localhost:8000/api/auth/logout/

For the change the password:
http://localhost:8000/api/rest-auth/password/change/

###You can reach this api for managing with tasks 

http://127.0.0.1:8000/api/task/


If you want to run test run this command:

```bash
docker-compose exec web python manage.py test
```
