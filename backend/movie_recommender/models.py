from django.db import models

# Create your models here.
class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    year = models.IntegerField()
    rating = models.FloatField()
    description = models.TextField()
    #image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title