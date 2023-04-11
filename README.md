

Clone the repo and then use the following command to start the app

```sh
1. docker-compose build
```

```sh
2. docker-compose up
```

## Migrations

When you want to migrate db changes

```sh
1. docker-compose run web python manage.py makemigrations
```

```sh
2. docker-compose run web python manage.py migrate
```

## Collect static

```sh
docker-compose exec web python manage.py collectstatic
```
