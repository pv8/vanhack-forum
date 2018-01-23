# VanHack Forum

The **VanhackForum** app is a tech project for [VanHack](http://www.vanhack.com/) [Talent Accelerator](https://docs.google.com/presentation/d/1_ctXv9Zn9n0ywpzdpvz7oRvWc_pe-FfmgOAkELxqbUk/edit) program.

Main app requisites for back-end developers:
- Landing page with all Posts
- Post's category
- Commenting system
- Login/Logout with permission to edit only owned Posts/Comments


## Tech stack

- Python 3.6
- Django 1.11.9
- Postgres 10.1 (production config)
- SQLite (development config)



## Running locally

Clone the repository to your local machine:

```bash
$ git clone git@github.com:pv8/vanhack-forum.git
```

Build the containers:

```bash
$ docker-compose -f compose-development.yml build
```

Run the migrations and create the super user:

```bash
$ docker-compose -f compose-development.yml run web migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, forum, sessions
Running migrations:
  Applying ...
$ docker-compose -f compose-development.yml run web createsuperuser
sername (leave blank to use 'root'): ...
Email address: ...
Password:
Password (again):
Superuser created successfully.
```

```bash
$ docker-compose -f compose-development.yml up
```

And go to http://127.0.0.1:8000 in your browser.

## Testing

The [Django Debug Toolbar](https://django-debug-toolbar.readthedocs.io) is available when running locally.


Running tests with [coverage](https://coverage.readthedocs.io) report:

```bash
$ docker-compose -f compose-development.yml run --service-ports web test -- --cov-config .coveragerc --cov=.
```


## Production config

Setup enviroment variables in `.env` (use [.env.example](https://github.com/pv8/vanhack-forum/blob/master/.env.example) as a starting point):

```bash
cp .env.example .env
```

All project configuration for production environment is on [docker production](https://github.com/pv8/vanhack-forum/blob/master/docker/production) directory.


## License

[MIT License](https://github.com/sibtc/django-beginners-guide/blob/master/LICENSE).
