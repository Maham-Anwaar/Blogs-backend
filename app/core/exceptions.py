# DRF
from rest_framework.exceptions import APIException


class FileTooBig(APIException):
    """This is a custom DRF exception, raised in file upload views. \
        This exception is raised when file size exceeds the set limit."""

    status_code = 413
    default_detail = "File size is too big."
    default_code = "file_size_too_big"


class CustomValidationError(APIException):
    """This is custom 400 error because the default DRF ValidationError throws \
        error in form of a list."""

    status_code = 400
    default_detail = "Bad Request"
    default_code = "bad_request"


class ServiceUnavailable(APIException):
    """This is a custom 503 error. \
        It is raised when a service is unavailable."""

    status_code = 503
    default_detail = "Check your internet connection, service is unavailable"
    default_code = "service_unavailable"
