from django.db import models

# Create your models here.
class Imageuploader(models.Model):
    photo=models.ImageField(upload_to="photofolder")
    date=models.DateField(auto_now_add=True)
