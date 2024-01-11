from django.db import models
from django.conf import settings


# Create your models here.
class Movie(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    COMEDY = 'CO'
    FANTASY = 'FA'
    ROMANCE = 'RO'
    GENRE_CHOICE = (
        (COMEDY, 'Comdey'),
        (FANTASY, 'Fantasy'),
        (ROMANCE, 'Romance'),
    )
    genre = models.CharField(max_length=10, choices=GENRE_CHOICE, default=COMEDY)
    score = models.FloatField()


class Comment(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.CharField(max_length=50)