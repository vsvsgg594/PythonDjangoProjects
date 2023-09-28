from django.db import models
from django.db import models

# Create your models here.


class Imageuploader(models.Model):
    photo=models.ImageField(upload_to="imagefolder")
    date=models.DateField(auto_now_add=True)

