from django.db import models

# Create your models here.
class ImageUploader(models.Model):
    photo=models.ImageField(upload_to="image")
    date=models.DateField(auto_now_add=True)
