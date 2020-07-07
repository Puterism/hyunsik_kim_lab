from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Home(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)
    content = RichTextUploadingField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Home'


class Site(models.Model):
    title = models.CharField(max_length=15)
    page_subtitle = models.CharField(max_length=200)
    address = models.CharField(max_length=300, null=True, blank=True)
    tel = models.CharField(max_length=300, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return 'Site'
