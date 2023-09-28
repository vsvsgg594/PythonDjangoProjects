from django.db import models

# Create your models here.
class Students(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField()
    address=models.TextField(null=True,blank=True)
    # image=models.ImageField()
    # file=models.FieldFile()


class Car(models.Model):
    car_name=models.CharField(max_length=100)
    speed=models.IntegerField()

    def __str__(self) -> str:
        return self.car_name


