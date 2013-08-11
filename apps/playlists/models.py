from django.db import models
from django.contrib.auth.models import User
import datetime


class Genre(models.Model):
    name = models.CharField(max_length=25)

    def __unicode__(self):
        return self.name


# class Tag(models.Model):
#     name = models.CharField(max_length=25)
#
#     def __unicode__(self):
#         return self.name


class Playlist(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(User)
    url = models.URLField()
    genre = models.ManyToManyField(Genre)
    #tags = models.ManyToManyField(Tag)
    date_added = models.DateField(default=datetime.date.today())

    def __unicode__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    favorites = models.ManyToManyField(Playlist, related_name='favorited')

    def __unicode__(self):
        return "{0} profile".format(self.user.username)

