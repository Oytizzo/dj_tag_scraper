from django.db import models


class SearchItem(models.Model):
    source = models.CharField(max_length=255)
    link = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.link[:50]
