from django.db import models

# Create your models here.

class Emp(models.Model):
    name=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    age=models.IntegerField()
    salary=models.IntegerField()
