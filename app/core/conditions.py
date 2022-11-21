# Standard Library
from datetime import datetime, timedelta, timezone

# Django
from django.conf import settings

# 3rd Party Libraries
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfparser import PDFParser, PDFSyntaxError
from PIL import Image


def is_pdf_file_valid(file):
    """A function that returns a boolean value depending on whether the \
        incoming file is a valid PDF or not."""
    try:
        parser = PDFParser(file)
        PDFDocument(parser)
    except PDFSyntaxError:
        return False
    return True


def is_file_size_valid(file, size):
    """A function that returns a boolean value depending on whether the incoming file crosses the allowed file\
        size or not."""
    if file.size / 1000000 > size:
        return False
    return True


def is_file_extension_valid(file, exts):
    """A function that returns a boolean value depending on whether the incoming file has a valid extension\
        or not."""
    ext = file.name.split(".")[-1]
    if ext not in exts:
        return False
    return True


def is_image_file_valid(file):
    """A function that returns a boolean value depending on whether the \
        incoming file is a valid image\
        or not."""
    try:
        Image.open(file)
    except IOError:
        return False
    return True


def is_email_link_valid(time):
    """A function that returns a boolean value depending on whether the \
        incoming link has expired or not."""
    it = time + timedelta(days=settings.EMAIL_LINK_EXPIRE)
    if it < datetime.now(timezone.utc):
        return False
    return True
