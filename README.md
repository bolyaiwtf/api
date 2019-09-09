# bolyai.wtf API

The project is a [Falcon](https://falconframework.org) application.

## Requirements

* Python
* [pipenv](https://github.com/pypa/pipenv)
* [gunicorn](https://gunicorn.org/)/[uWSGI](https://uwsgi-docs.readthedocs.io/en/latest/) for *nix or [waitress](https://docs.pylonsproject.org/projects/waitress/en/stable/) for Windows

## Getting Started

Clone the repository

```sh
git clone git@github.com:bolyaiwtf/api.git bolyaiwtf-api
cd bolyaiwtf-api
```

Install the dependencies

```sh
pipenv install
```

Activate the environment

```sh
pipenv shell
```

Run - on Linux

```sh
gunicorn bolyaiwtf:api
```

[steps on how to add content will be described here later]

Run - on Windows

```sh
waitress bolyaiwtf:api
```

The app will listen at http://127.0.0.1:8080

## What?

bolyai.wtf is a JOKE PROJECT. It is a random message generator specifically tied to student life in the Bolyai Farkas High School from Marosvásárhely, Romania. bolyai.wtf is in no way affiliated with the high school.

## License

MIT.
