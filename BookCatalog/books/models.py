from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    availability = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} by {self.author}"
# Create your models here.
