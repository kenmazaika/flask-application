# Flask Application


## Run the Application

```
FLASK_APP=flaskr FLASK_ENV=development flask
```

## Initialize the Database

```
FLASK_APP=flaskr FLASK_ENV=development flask init-db
```

## Run test suite

```
pytest -v
```

## Run individual test

```
pytest -v -k test_hello
```