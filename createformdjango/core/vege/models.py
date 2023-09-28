from django.db import models

# Create your models here.
class Receipes(models.Model):
    receipe_name=models.CharField(max_length=100)
    receipe_des=models.TextField()
    receipe_image=models.ImageField(upload_to="receipe")