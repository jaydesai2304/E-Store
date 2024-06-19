from django.db import models

class Register(models.Model):
    fname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone_no = models.IntegerField(default='')
    password = models.CharField(max_length=100)
    c_password = models.CharField(max_length=100)
    otp = models.CharField(max_length=4, null=True, blank=True)
