from django.db import models
from django.contrib.auth import User

# Create your models here.
class Loginpage(models.Model):
    user=models.ForeignKey(User ,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    passwd=models.CharField(max_length=100)
