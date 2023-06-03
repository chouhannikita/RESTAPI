from django.db import models

# Create your models here.
class Emp(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    add=models.CharField(max_length=30)
    def __str__(self):
        return self.name
