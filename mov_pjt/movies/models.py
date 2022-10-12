from random import choices
from django.db import models
from django.conf import settings
# Create your models here.

class Movie(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    audience = models.IntegerField()
    release_date = models.DateField(auto_now_add=False)
    genre_Choice = (('Comedy','Comedy'),('Action','Action'),('Romance','Romance'),('Adventure','Adventure'),('Crime','Crime'),('War','War'),('Drama','Drama'),('Horror','Horror'),('Science Fiction ','Science Fiction '),('Musicals','Musicals'),('Historical','Historical'))
    genre = models.CharField(max_length=20, choices=genre_Choice)
    score = models.FloatField()
    poster_url = models.TextField()
    description = models.TextField()
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='likes_movies')

    def __str__(self):
        return self.title


class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment
