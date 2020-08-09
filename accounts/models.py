from django.db import models
from django.db import models


# Create your models here.


class Brand(models.Model):
    brand = models.CharField(max_length=20)

    def __str__(self):
        return self.brand


class Shop(models.Model):
    b_type = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.CharField(max_length=50)
    price = models.BigIntegerField()
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.model
