from django.db import models

class Register(models.Model):
    fname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone_no = models.IntegerField(default='')
    password = models.CharField(max_length=100)
    c_password = models.CharField(max_length=100)
    otp = models.CharField(max_length=4, null=True, blank=True)

class MenProduct(models.Model):
    name = models.CharField(max_length=100)
    discription = models.CharField(max_length=100,default='')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='Menproducts/', default='')
    image1 = models.ImageField(upload_to='Menproducts/', default='')
    image2 = models.ImageField(upload_to='Menproducts/', default='')

class WomenProduct(models.Model):
    name = models.CharField(max_length=100)
    discription = models.CharField(max_length=100,default='')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='Menproducts/', default='')
    image1 = models.ImageField(upload_to='Menproducts/', default='')
    image2 = models.ImageField(upload_to='Menproducts/', default='')

class KidsProduct(models.Model):
    name = models.CharField(max_length=100)
    discription = models.CharField(max_length=100,default='')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='Menproducts/', default='')
    image1 = models.ImageField(upload_to='Menproducts/', default='')
    image2 = models.ImageField(upload_to='Menproducts/', default='')

class FashionProduct(models.Model):
    name = models.CharField(max_length=100)
    discription = models.CharField(max_length=100,default='')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='Menproducts/', default='')
    image1 = models.ImageField(upload_to='Menproducts/', default='')
    image2 = models.ImageField(upload_to='Menproducts/', default='')
    