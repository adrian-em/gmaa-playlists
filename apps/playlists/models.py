from django.db import models
from django.contrib.auth.models import User


class Genre(models.Model):
    name = models.CharField(max_length=25)


class Tag(models.Model):
    name = models.CharField(max_length=25)


class Playlist(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(User)
    url = models.URLField()
    genre = models.ForeignKey(Genre)
    tags = models.ManyToManyField(Tag)
