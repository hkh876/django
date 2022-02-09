from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=255)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    image_path = models.URLField()
    release_date = models.DateField()
    overview = models.TextField()

class Genre(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_genre')
    name = models.CharField(max_length=50)
