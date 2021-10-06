from django.db import models


class Blog(models.Model):
    image = models.ImageField(upload_to="blog_images/" , null=True)
    title = models.CharField(max_length=120)
    description = models.TextField()
    likes = models.IntegerField()
    reposts = models.IntegerField()