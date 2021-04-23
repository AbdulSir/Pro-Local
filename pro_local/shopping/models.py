from django.db import models

# Create your models here.

class Shop(models.Model):
    s_name = models.CharField(null=False, blank=False, max_length=80, unique=True)
    address = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    province = models.CharField(max_length=120)
    s_link = models.CharField(max_length=1000, default="#")
    postal_code = models.CharField(max_length=6)
    distance = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.s_name

class Product(models.Model):
    p_name = models.CharField(null=False, blank=False, max_length=80, unique=True)
    p_keys = models.CharField(null=False, blank=False, max_length=160, unique=False)
    p_link = models.CharField(max_length=1000)
    price = models.DecimalField(decimal_places=2, null=False, blank=False, max_digits=9)
    s_FK = models.ForeignKey(Shop, on_delete=models.CASCADE)
    img = models.CharField(max_length=1000)

    def __str__(self):
        return self.p_name



