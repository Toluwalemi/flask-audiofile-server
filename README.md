# `AUDIO SERVER` service

`Audio service` service is a Python library that simulates the behavior of an audio file server.

## Requirements

You must install [docker](https://get.docker.com) to use the compose file.

## Structure

```text
.
├── migrations
├── src
│   ├── api
│   │   ├── routes
│   │   ├── tests
│   ├── db
│   ├── __init__.py
│   ├── config.py
├── .dockerignore
├── .gitignore
├── docker-compose-dev.yml
├── Dockerfile-dev
├── entrypoint.sh
├── manage.py
├── .README.md
├── .requirements.txt
```

> To add/modify the application environment variables and host ports check `docker-compose-dev.yml`
e.g ports: `<host>:<container>`

## General Usage

> * Ensure that you set the necessary secret keys

```bash
Clone the repository
```

* Build and startup container in detached

```bash
 docker-compose -f docker-compose-dev.yml up -d --build
```

* Run the tests

```
 docker-compose -f docker-compose.yml run audio python manage.py test
```
* Run the test coverage

```
 docker-compose -f docker-compose.yml run audio python manage.py coverage
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
Kindly refer to the license file