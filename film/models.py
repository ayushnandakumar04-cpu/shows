from django.db import models
from account.models import User
from datetime import datetime,timedelta
class Movies(models.Model):

    LANGUAGE_CHOICES = [
        ('EN', 'English'),
        ('ML', 'Malayalam'),
        ('TA', 'Tamil'),
        ('HI', 'Hindi'),
        ('TE', 'Telugu'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    genre = models.CharField(max_length=100)
    language = models.CharField(
        max_length=2,
        choices=LANGUAGE_CHOICES
    )
    release_date = models.DateField()
    duration = models.PositiveIntegerField()
    rating = models.FloatField(default=0.0)
    director = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,null=True
    )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):

        end_date_time = datetime.combine(
            datetime.today().date(),
            self.start_time
        ) + timedelta(minutes=self.duration)

        self.end_time = end_date_time.time()

        return super().save(*args, **kwargs)