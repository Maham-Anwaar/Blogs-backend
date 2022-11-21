# Standard Library
from datetime import date
from typing import Any, Optional, Union

# Backend Apps
from core.constants import A_401_AUTH_FAILED

# Django Ninja
from ninja import Field, Schema

# 3rd Party Libraries
from pydantic import UUID4


class RequiredName(Schema):
    """This schema/serializer class is an abstract class which can be \
        \
        inherited where ever we need to serialize the name\
        property of a model object."""

    name: str


class RequiredID(Schema):
    """This schema/serializer class is an abstract class which can be \
        \
        inherited where ever we need to serialize the uuid\
        of a model object."""

    id: UUID4


class RequiredOrder(Schema):
    """This schema/serializer class is an abstract class which can be \
        inherited where ever we need to serialize the order\
        of a model object."""

    order: int


class RequiredCamelCaseDates(Schema):
    """This schema/serializer class is an abstract class which can be \
        inherited where ever we need to serialize the meta\
        dates of a model object."""

    created_at: date
    modified_at: date


class Pagination(Schema):
    """This schema/serializer class is an abstract class which can be \
        inherited where ever we need to paginate the queryset\
        of a model."""

    count: int = Field(..., example=4)
    previous: Union[str, None]
    next: Union[str, None]
    results: Optional[list[dict[str, Any]]] = Field(
        ...,
        example=[{"prop1": "uuid", "prop2": "date", "prop3": "str", "prop4": "int", "prop5": "bool", "prop6": "etc"}],
    )


class Error401(Schema):
    """This schema/serializer class is an abstract class which can be \
        inherited where ever we need to send the error message\
        back to the client."""

    detail: str = Field(default=A_401_AUTH_FAILED)


class Error(Schema):
    """This schema/serializer class is an abstract class which can be \
        inherited where ever we need to send the error message\
        back to the client."""

    detail: str


class MissingErrorDetails(Schema):
    """This schema/serializer class is an abstract class which can be \
        inherited where ever we need to send 422 error msg \
        back to client."""

    type: str
    msg: str
    loc: list[str]


class Error422(Schema):
    """This schema/serializer class is an abstract class which can be \
        inherited where ever we need to send 422 error msg \
        back to client."""

    detail: list[MissingErrorDetails]
