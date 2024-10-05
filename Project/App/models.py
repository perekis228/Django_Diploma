from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    description = models.TextField()
    genre = models.CharField(max_length=15)

    def __str__(self):
        return self.title

class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    age = models.IntegerField()
    admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username