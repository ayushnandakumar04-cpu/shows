from django.db import models
from film.models import Movies
from shows import settings


class Song(models.Model):

    LANGUAGE_CHOICES = [
        ('ML', 'Malayalam'),
        ('EN', 'English'),
        ('TA', 'Tamil'),
        ('HI', 'Hindi'),
        ('TE', 'Telugu'),
    ]

    title = models.CharField(max_length=200)
    singer = models.CharField(max_length=100)
    album = models.CharField(max_length=200, blank=True)
    language = models.CharField(
        max_length=2,
        choices=LANGUAGE_CHOICES
    )
    movies = models.ForeignKey(
        Movies,
        on_delete=models.CASCADE
    )
    duration = models.PositiveIntegerField()  
    start_time = models.TimeField()
    end_time = models.TimeField(null=True, blank=True)

    created_by = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE,
    null=True,
    blank=True
)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title