import os

from .default import *

SECRET_KEY = os.environ.get("SECRET_KEY")

DEBUG = int(os.environ.get("DEBUG", default=0))

# 'DJANGO_ALLOWED_HOSTS' should be a single string of hosts with a space between each.
# For example: 'DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]'
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")
CSRF_TRUSTED_ORIGINS = os.environ.get("CSRF_TRUSTED_ORIGINS").split(" ")

INSTALLED_APPS += [
    # third party
    "rest_framework",
    "rest_framework_simplejwt",
    "rest_framework_simplejwt.token_blacklist",
    # custom
    "user",
    "db_data",
    "core",
]

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("SQL_DATABASE", BASE_DIR / "db.sqlite3"),
        "USER": os.environ.get("SQL_USER", "user"),
        "PASSWORD": os.environ.get("SQL_PASSWORD", "password"),
        "HOST": os.environ.get("SQL_HOST", "localhost"),
        "PORT": os.environ.get("SQL_PORT", "5432"),
        "ATOMIC_REQUESTS": True,
    }
}

STATIC_URL = "/static/"
STATIC_ROOT = "/home/app/staticfiles"

MEDIA_URL = "/media/"
MEDIA_ROOT = "/home/app/mediafiles"

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": ["rest_framework_simplejwt.authentication.JWTAuthentication"],
    # "DEFAULT_RENDERER_CLASSES": [
    #     "rest_framework.renderers.JSONRenderer",
    #     "core.renderers.OnlyRawBrowsableAPIRenderer",
    # ],
    # "PAGE_SIZE": 15,
}

del AUTH_PASSWORD_VALIDATORS[-3:]
AUTH_PASSWORD_VALIDATORS.append({"NAME": "db_data.validations.PasswordValidation"})

AUTH_USER_MODEL = "db_data.BaseUser"
