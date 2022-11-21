from itertools import chain
from typing import Any

from django.db.models import QuerySet
from django.http import HttpRequest


def to_dict(instance):
    """This function converts a model object into a key-value pair\
         of it's attributes."""
    opts = instance._meta
    data = {}
    for f in chain(opts.concrete_fields, opts.private_fields):
        data[f.name] = f.value_from_object(instance)
    for f in opts.many_to_many:
        data[f.name] = [i.id for i in f.value_from_object(instance)]
    return data


def paginate(qs: QuerySet, page: int) -> list:
    """Returns a paginated list of django QuerySet."""
    page_size = 15
    offset = (page - 1) * page_size

    return list(qs[offset : offset + page_size])


def get_paginated_response_dict(request: HttpRequest, data: list[Any], qs_count: int, cpage: int):
    """Returns a paginated list of django QuerySet."""
    page_size = 15
    offset = (cpage - 1) * page_size
    next = request.build_absolute_uri(request.get_full_path()).replace(f"p={cpage}", f"p={cpage + 1}")
    previous = request.build_absolute_uri(request.get_full_path()).replace(f"p={cpage}", f"p={cpage - 1}")
    if offset + page_size >= qs_count:
        next = None
    if cpage == 1:
        previous = None

    return {"count": qs_count, "next": next, "previous": previous, "results": data}
