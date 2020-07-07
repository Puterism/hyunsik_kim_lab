from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

import datetime


def get_now_year():
    return datetime.date.today().year


class Research(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200, null=True, blank=True)
    content = RichTextUploadingField()
    order = models.AutoField(primary_key=True, editable=True)
    year = models.IntegerField(default=get_now_year)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
