from django.db import models

# Create your models here.

 class Shop(models.Model):
     s_name = models.CharField(null=False, blank=False, max_length=80, unique=True)
     p_FK = models.ForeignKey(Product, on_delete=models.CASCADE)
     address = models.CharField(max_length=120)
     city = models.CharField(max_length=120)
     province = models.CharField(max_length=120)
     postal_code = models.CharField(max_length=6)

#     def __str__(self):
# 		    return self.w_name

 class Product(models.Model):

     p_name = models.CharField(null=False, blank=False, max_length=80, unique=True)
     p_keys = models.CharField(null=False, blank=False, max_length=160, unique=True)
     price = models.DecimalField(decimal_places=2, null=False, blank=False, max_digits=9)
     s_FK = models.ForeignKey(Shop, on_delete=models.CASCADE)
     img = models.ImageField(blank=null, null=false)
    #pip install Pillow for the images to work

    # https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&origins=H4N+3B6&destinations=H4N+3K1&key=AIzaSyATsUAiN8HGEmtdItkO3n5E74FEKAelw5o




