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

Create the database by running [Django migrations](https://docs.djangoproject.com/en/1.11/ref/django-admin/#django-admin-migrate)):

```bash
$ docker-compose -f compose-development.yml run web migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, forum, sessions
Running migrations:
  Applying ...
```

Create a superuser (Optional):

```bash
$ docker-compose -f compose-development.yml run web createsuperuser
sername (leave blank to use 'root'): ...
Email address: ...
Password:
Password (again):
Superuser created successfully.
```

Start the application:

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

### Deploying oh [Heroku](https://www.heroku.com/)

1. Create a free [mailgun](https://www.mailgun.com/) account.

2. Install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) and setup the environment:

```bash
$ heroku create --buildpack https://github.com/heroku/heroku-buildpack-python
$ heroku addons:create heroku-postgresql:hobby-dev
$ heroku pg:promote DATABASE_URL
$ heroku addons:create heroku-redis:hobby-dev
$ heroku addons:create mailgun
$ heroku config:set DJANGO_ADMIN_URL="$(openssl rand -base64 32)"
$ heroku config:set DJANGO_SECRET_KEY="$(openssl rand -base64 64)"
$ heroku config:set DJANGO_SETTINGS_MODULE='settings.production'
$ heroku config:set DJANGO_ALLOWED_HOSTS='.herokuapp.com'
$ heroku config:set DJANGO_MAILGUN_API_KEY=<mailgun API key>
$ heroku config:set MAILGUN_SENDER_DOMAIN=sandbox<....>.mailgun.org
```

3. Add herku as remote git repository and push the code:
```bash
$ git add remote heroku https://git.heroku.com/<heroku-app-name>.git
$ git push heroku master
```

4. Setup the application:
```bash
$ heroku run python manage.py migrate
$ heroku run python manage.py createsuperuser
```

## License

[MIT License](https://github.com/sibtc/django-beginners-guide/blob/master/LICENSE).
