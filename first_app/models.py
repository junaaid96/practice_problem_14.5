from django.db import models

# Create your models here.


class MyModel(models.Model):
    movie_title = models.CharField(max_length=150)
    release_year = models.IntegerField()
    genre = models.CharField(max_length=50)
    director = models.CharField(max_length=150)
    rating = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.movie_title
