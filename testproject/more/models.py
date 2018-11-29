from django.db import models
from django.forms.models import modelform_factory


# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=30)


class Author(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=40)


class Podcast(models.Model):
    image = models.ImageField('Photo', upload_to='image_podcast', default='', blank=True)
    title = models.CharField(max_length=255)
    text = models.TextField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publish_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title
