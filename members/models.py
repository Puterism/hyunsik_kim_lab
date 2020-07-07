import os
from uuid import uuid4
from django.db import models


def photo_upload_to(instance, filename):
    path_name = 'members'
    generated_uuid = uuid4().hex
    extension = os.path.splitext(filename)[-1].lower()
    return '/'.join([
        path_name, generated_uuid + extension,
    ])


class Position(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Member(models.Model):
    name = models.CharField(max_length=30)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    # position = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    photo = models.ImageField(upload_to=photo_upload_to, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name




