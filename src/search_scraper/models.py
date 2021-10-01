from django.db import models
from django.utils import timezone


class SearchItem(models.Model):
    source = models.CharField(max_length=255)
    link = models.TextField()
    title = models.CharField(max_length=255, null=True)
    publish_date = models.DateField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.link[:50]
