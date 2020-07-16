from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models import Max


class Publication(models.Model):
    content = RichTextUploadingField()
    order = models.IntegerField(default=1)
    label = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

    def save(self, update=False, *args, **kwargs):
        publication_order_max = Publication.objects.aggregate(Max('order'))['order__max']

        if not update:
            if publication_order_max and publication_order_max > 0:
                self.order = publication_order_max + 1

        super(Publication, self).save(*args, **kwargs)
