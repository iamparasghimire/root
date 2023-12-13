from django.db import models

# Create your models here.

class Crime(models.Model):
    year = models.IntegerField()
    crime = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.crime