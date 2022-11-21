# Django
from db_data.models.base_user import BaseUser
from django.contrib.auth.models import update_last_login

# DRF
from rest_framework import exceptions

# 3rd Party Libraries
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.views import TokenObtainPairView


class TokenSerializer(TokenObtainPairSerializer):
    """
    Needed to re-create this because we want to be able to throw custom error
    message for email and password.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def validate(self, attrs):
        try:
            user = BaseUser.objects.get(email=attrs[self.username_field])
        except BaseUser.DoesNotExist:
            raise exceptions.AuthenticationFailed({"email": "EMAIL_DOESNT_EXIST"})

        # Check if password is valid for the user
        if attrs.get("password") and not user.check_password(attrs["password"]):
            raise exceptions.AuthenticationFailed({"password": "INVALID_PASSWORD"})

        # If the user is inactive, raise an exception
        if not api_settings.USER_AUTHENTICATION_RULE(user):
            raise exceptions.AuthenticationFailed({"email": "NEED_ACTIVATION"})

        refresh = self.get_token(user)
        data = {}

        data["access_token"] = str(refresh.access_token)
        data["refresh_token"] = str(refresh)

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, user)

        return data


class API(TokenObtainPairView):
    """This API returns Access and Refresh token for existing user."""

    serializer_class = TokenSerializer
