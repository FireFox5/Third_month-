from django.db import models
from django.urls import reverse


class Blog(models.Model):
    image = models.ImageField(upload_to="blog_images/", null=True)
    title = models.CharField(max_length=120, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    likes = models.IntegerField(default=0)
    reposts = models.IntegerField(default=0)

    def get_absolute_url(self):
        return f"/blog/{self.pk}/"
