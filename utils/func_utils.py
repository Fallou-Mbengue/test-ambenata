# utils.func_utils.py

import os
import string
import random

from django.db import models
from django.utils.text import slugify


def random_string_generator(size=6, carac=string.digits):
    return ''.join(random.choice(carac) for _ in range(size))


def unique_slug_generator(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.first_name)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()

    if qs_exists:
        new_slug = f"{slug}-{random_string_generator(6)}"
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug


def save_avatar_file(instance, filename):
    upload_to = 'users/'
    ext = filename.split('.')[-1]
    if instance.avatar:
        filename = f"avatar_{instance.first_name}.{ext}"

    return os.path.join(upload_to, filename)


def save_project_file(instance, filename):
    upload_to = 'project/'
    ext = filename.split('.')[-1]
    if instance.avatar:
        filename = f"pj_{instance.title}.{ext}"

    return os.path.join(upload_to, filename)
