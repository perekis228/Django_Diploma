from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    description = models.TextField()
    genre = models.CharField(max_length=15)

    def __str__(self):
        return self.title