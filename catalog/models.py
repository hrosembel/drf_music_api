from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(null=True, blank=True, help_text='Give some info about the artist')
    favorite = models.BooleanField(default=False)
    last_modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

class Genre(models.Model):
    name = models.CharField(max_length=100)

class Album(models.Model):
    title = models.CharField(max_length=100)
    release_on = models.DateTimeField(blank=True, null=True)
    artists = models.ManyToManyField('Artist')
    genres = models.ManyToManyField('Genre')

class Song(models.Model):
    title = models.CharField(max_length=100)
    album = models.ForeignKey('Album', on_delete=models.CASCADE)
    lyrics = models.TextField(null=True, blank=True, help_text='Lyrics of the song')
    duration = models.FloatField(default=0, blank=True)