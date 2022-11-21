from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from user.authentication.api import create_tokens

urlpatterns = [
    # auth
    path("token/", create_tokens.API.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
