from django.db import models
from film.models import Movies
from account.models import User
# Create your models here.
class Reviews(models.Model):
    movie=models.ForeignKey(Movies,on_delete=models.CASCADE)
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    message=models.TextField()
    rating=models.FloatField()
    
    def __str__(self):
        return f"{self.movie.title} - {self.rating}"