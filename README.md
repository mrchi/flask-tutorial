# flask-tutorial

A Flask application named Flaskr, written by following [Tutorial in Flask Documents](http://flask.pocoo.org/docs/1.0/tutorial/).

Different from [official example](https://github.com/pallets/flask/tree/1.0.2/examples/tutorial), I use Flask extensions. such as:

- Flask-SQLAlchemy
- Flask-Login
- Flask-Migrate

## commands

### database

```
docker run -d \
    --name flaskr-db \
    -e POSTGRES_USER=flask \
    -e POSTGRES_PASSWORD=flask123 \
    -e POSTGRES_DB=flaskr \
    -p 127.0.0.1:5432:5432 \
    postgres
```

```
psql -U flask -d flaskr -p 5432 -h localhost
```

### testing

```
coverage run -m pytest
coverage report
coverage html
```

### build and install

```
pip install wheel
python setup.py bdist_wheel
```

```
pip install flaskr-1.0.0-py3-none-any.whl
export FLASK_APP=flaskr
flask init-db
flask fake
flask run
```

## TODO

- ~~[ ] Use JSON-Schema validating params;~~ (It's convenient for API, not for templates.)
- [x] Add CLI command for generating fake data;
- [x] Add testing for CLI command;
