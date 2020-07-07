import os
from uuid import uuid4
from django.db import models


def photo_upload_to(instance, filename):
    path_name = 'professor'
    generated_uuid = uuid4().hex
    extension = os.path.splitext(filename)[-1].lower()
    return '/'.join([
        path_name, generated_uuid + extension,
    ])


class Profile(models.Model):
    name = models.CharField(max_length=30)
    name_kor = models.CharField(max_length=30)
    position = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    email = models.EmailField()
    photo = models.ImageField(upload_to=photo_upload_to, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Menu(models.Model):
    header = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.header


class Item(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    year = models.CharField(max_length=50, null=True, blank=True)
    title = models.CharField(max_length=50, null=True, blank=True)
    subtitle = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return ''.join([self.year + ', ' if self.year else '', self.title + ', ' if self.title else ', ', self.subtitle if self.subtitle else ''])
