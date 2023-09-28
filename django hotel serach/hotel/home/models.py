from django.db import models

# Create your models here.

class Amentites(models.Model):
    amenity=models.ManyToManyField()
    create_at=models.DateField(auto_now_add=True)
    update_at=models.DateField(auto_now=True)


class Hotel(models.Model):
    hotel_name=models.CharField(max_length=100)
    hotel_description=models.TextField()
    hotel_price=models.IntegerField()
    amentites=models.ManyToManyField(Amentites)
    banner_img=models.ImageField(upload_to="photo")
    create_at=models.DateField(auto_now_add=True)
    update_at=models.DateField(auto_now=True)





class HotelImage(models.Model):
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="photo")
    create_at=models.DateField(auto_now_add=True)
    update_at=models.DateField(auto_now=True)


