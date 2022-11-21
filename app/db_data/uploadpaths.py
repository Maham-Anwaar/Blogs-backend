# Standard Library
import os
from uuid import uuid4


def upload_assignment_file(instance, filename):
    """Generate file path for assignments."""
    ext = filename.split(".")[-1]
    filename = f"assignment_{uuid4()}.{ext}"
    return os.path.join("assignments/files/", filename)


def upload_material_file(instance, filename):
    """Generate file path for assignments."""
    ext = filename.split(".")[-1]
    filename = f"assignment_{uuid4()}.{ext}"
    return os.path.join("lectures/files/", filename)
