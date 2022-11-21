# Standard Library
import re

# 3rd Party Libraries
import pytz

# Backend Apps
from core.conditions import (
    is_file_extension_valid,
    is_file_size_valid,
    is_image_file_valid,
    is_pdf_file_valid,
)
from core.exceptions import FileTooBig

# Django
from django.core import exceptions

URL_REGEX = r"(http(s)?:\/\/.)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)"


def name_validation(name):
    """Validate name fields."""
    if len(name) < 2:  # removes spaces and then checks the length of string.
        raise exceptions.ValidationError(
            "Must be at least 2 characters\
             or long"
        )
    full_name_pattern = r"^[A-Za-z0-9\-_.\s]+$"

    if re.match(full_name_pattern, name) is None:
        raise exceptions.ValidationError("NAME_VALIDATION_ERROR")


def email_validation(email):
    """Validate email fields."""
    if len(email) < 6:
        raise exceptions.ValidationError(
            "Must be at least 6\
             characters or long"
        )

    spaces = r"\s"
    if re.match(spaces, email):
        raise exceptions.ValidationError("Spaces are not allowed.")

    sign_pattern = r".*@.*"

    if re.match(sign_pattern, email) is None:
        raise exceptions.ValidationError("Must contain @")

    name = email.split("@")[0]
    name_pattern = r"^[A-Za-z0-9]$|^[A-Za-z0-9][A-Za-z0-9._+-]*[A-Za-z0-9]$"

    if re.match(name_pattern, name) is None:
        raise exceptions.ValidationError(
            f"{name} can only \
            contain ._+- symbols and it cannot start & end with the symbols"
        )

    domain = email.split("@")[1]
    domain_special_characters_pattern = r"^[A-Za-z0-9]$|^[A-Za-z0-9][A-Za-z0-9.-]*[a-zA-Z0-9]$"

    mid = domain.split(".")

    if len(mid) == 1:
        raise exceptions.ValidationError("Invalid email address.")

    del mid[-1]
    mid = ".".join(mid)

    if re.match(domain_special_characters_pattern, mid) is None:
        raise exceptions.ValidationError(
            f"{mid} can only\
             contain .- symbols and it cannot start & end with -"
        )

    last = domain.split(".")[-1]
    domain_length_pattern = r"^[A-Za-z0-9]{2,4}$"
    if re.match(domain_length_pattern, last) is None:
        raise exceptions.ValidationError(
            f"{last} can only \
            be alphanumeric and 2 to 4 characters long."
        )


class PasswordValidation:
    """Validate password fields."""

    @classmethod
    def validate(cls, password, user=None):
        regex = re.compile(r"[#$%^&*()<>/|}{~:]")

        if len(password) < 8:
            raise exceptions.ValidationError("Must be atleast 8 characters long.")

        if password.isdigit():
            raise exceptions.ValidationError("Can't be entirely numeric.")

        if not any(char.islower() for char in password):
            raise exceptions.ValidationError("Must contain at least one lowercase letter")

        if not regex.search(password) is None:
            raise exceptions.ValidationError("Can only contain spaces and @!-_?+ symbols.")

        if not any(char.isdigit() for char in password):
            raise exceptions.ValidationError("Must contain at least one digit.")

    def get_help_text(self):
        return "Your password should be valid."


def phone_validation(phone):
    """Validate phone number."""
    symbol_regex = r"^[\d+\- \+\(\)]*$"
    country_code_regex = r"^\+[1-9][\d+\- \+\(\)]*$"
    if re.match(symbol_regex, phone) is None:
        raise exceptions.ValidationError("Only digits, spaces, (, ), +, - symbols are allowed.")
    if re.match(country_code_regex, phone) is None:
        raise exceptions.ValidationError("Invalid country code.")


def timezone_validation(tz):
    """Check if the timezone is valid."""
    if tz not in pytz.all_timezones:
        raise exceptions.ValidationError(f"Unknown Timezone: {tz}")


def url_validation(addr):
    """Validator for URL."""
    if re.match(URL_REGEX, addr) is None:
        raise exceptions.ValidationError("URL is invalid.")


def non_negative_validation(val):
    """Validation for numbers; to make sure they are positive."""
    if val and val < 0:
        raise exceptions.ValidationError("Should be a positive number.")


def percentage_validation(val):
    """Validator for percentage."""
    if val and val > 100:
        raise exceptions.ValidationError("Percentage should be less than equal to 100")
    non_negative_validation(val)


def image_validation(img):
    """Validate jpg and png image files along with their size."""
    if not is_file_size_valid(img, 3):
        raise FileTooBig("Should not be greater than 3 MB.")
    if not is_file_extension_valid(img, ["jpg", "jpeg", "png"]):
        raise exceptions.ValidationError("Should be either a JPG or a PNG.")
    if not is_image_file_valid(img):
        raise exceptions.ValidationError("Invalid image.")


def document_validation(file):
    """Validate pdf file along with their size."""
    if not is_file_size_valid(file, 3):
        raise FileTooBig("Should not be greater than 3 MBs.")
    if not is_file_extension_valid(file, ["pdf"]):
        raise exceptions.ValidationError("Should be a PDF.")
    if not is_pdf_file_valid(file):
        raise exceptions.ValidationError("Invalid PDF.")


def file_validation(file):
    """Validate file to be a valid pdf or jpg/png with its size."""
    ext = file.name.split(".")[-1]
    if ext == "pdf":
        document_validation(file)
    elif ext == "png" or ext == "jpg" or ext == "jpeg":
        image_validation(file)
    else:
        raise exceptions.ValidationError("Only PDF, PNG and JPG files are allowed.")


def order_validation(value):
    """Validates the order to be non-zero wherever we are working\
         with a model where order of rows is important."""
    if value == 0:
        raise exceptions.ValidationError("Should be greater than 0.")
