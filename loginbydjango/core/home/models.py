from django.db import models
from django.contrib.auth.models import User

# Create your models here.
def loginpage(request):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    passwd=models.CharField(max_length=100)
