from django.db import models


# Create your models here.
class Movie(models.Model):
    name=models.CharField(max_length=500)
    description=models.TextField(max_length=10000)
    image=models.ImageField(upload_to='images/')
    screen_shot=models.ImageField(blank=True)
    trailer=models.FileField(upload_to='videos/', null=True)
    movie_length=models.CharField(max_length=50)
    release_date=models.DateField()
    movie_rate=models.CharField(max_length=100)
    imdb_rating=models.CharField(max_length=100)
    movie_director=models.CharField(max_length=200)
    movie_actor=models.CharField(max_length=1000)
    category=models.CharField(max_length=500)
    movie_language=models.CharField(max_length=1000)
    movie_quality=models.CharField(max_length=100)
    movie_link=models.TextField(max_length=10000)
    movie_size=models.CharField(max_length=100)


    def __str__(self):
        return self.name
         
class MovieImage(models.Model):
    screenshot=models.ForeignKey(Movie, default=None, on_delete=models.CASCADE)
    screen_shot=models.ImageField(upload_to='screenshot/')

    def __str__(self):
        return self.screenshot.name