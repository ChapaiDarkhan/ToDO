# Book
Create and update book information

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


###You can reach this api for managing with books 

http://127.0.0.1:8000/api/book/


If you want to run test run this command:

```bash
./manage.py test
```

For running test with docker-compose:
```bash
docker-compose exec web python manage.py test
```
