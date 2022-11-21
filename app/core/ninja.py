# Standard Library
from typing import Optional, Union

# Django
from django.contrib.auth.models import AnonymousUser
from django.http import HttpRequest

# Django Ninja
from ninja import NinjaAPI
from ninja.errors import HttpError
from ninja.security import APIKeyHeader

# 3rd Party Libraries
from rest_framework_simplejwt.authentication import JWTAuthentication


# Custom JWT Authentication Class for Ninja
class JWTAuthRequired(APIKeyHeader):
    """
        This authentication class checks for JWT token attached in the \
        header of each request for django-ninja to allow the request \
        to proceed to the api views.
    """

    param_name = "Authorization"

    def authenticate(self, request: HttpRequest, token: str) -> Optional[Union[bool, HttpError]]:
        """
        This function re-uses the logic of our jwt authentication package.
        """

        jwt_authenticator = JWTAuthentication()
        try:
            request.user, _ = jwt_authenticator.authenticate(request)
        except Exception:
            request.user = AnonymousUser()
        return True


# Ninja app instance

ninja_api_v1 = NinjaAPI(
    version="1.0.0",
    title="Arisbe API V1.0",
    auth=JWTAuthRequired(),
    urls_namespace="api-v1",
)

# Routes start

# ninja_api_v1.add_router("/attrs/", custom_attrs_router)


# Routes finish
