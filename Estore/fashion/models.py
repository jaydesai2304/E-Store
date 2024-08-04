from django.db import models

class Register(models.Model):
    fname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone_no = models.IntegerField(default='')
    password = models.CharField(max_length=100)
    c_password = models.CharField(max_length=100)
    otp = models.CharField(max_length=4, null=True, blank=True)

class ProductType(models.TextChoices):
    men = "men"
    women = "women"
    kids = "kids"
    fashion = "fashion"
    gadget = "gadget"
    other = "other"

class MenProduct(models.Model):
    name = models.CharField(max_length=100)
    discription = models.CharField(max_length=100,default='')
    product_type = models.CharField(max_length=50, choices=ProductType.choices, default=ProductType.other)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='Menproducts/', default='')
    image1 = models.ImageField(upload_to='Menproducts/', default='')
    image2 = models.ImageField(upload_to='Menproducts/', default='')

class WomenProduct(models.Model):
    name = models.CharField(max_length=100)
    discription = models.CharField(max_length=100,default='')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    product_type = models.CharField(max_length=50, choices=ProductType.choices, default=ProductType.other)
    image = models.ImageField(upload_to='Menproducts/', default='')
    image1 = models.ImageField(upload_to='Menproducts/', default='')
    image2 = models.ImageField(upload_to='Menproducts/', default='')

class KidsProduct(models.Model):
    name = models.CharField(max_length=100)
    discription = models.CharField(max_length=100,default='')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    product_type = models.CharField(max_length=50, choices=ProductType.choices, default=ProductType.other)
    image = models.ImageField(upload_to='Menproducts/', default='')
    image1 = models.ImageField(upload_to='Menproducts/', default='')
    image2 = models.ImageField(upload_to='Menproducts/', default='')

class FashionProduct(models.Model):
    name = models.CharField(max_length=100)
    discription = models.CharField(max_length=100,default='')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    product_type = models.CharField(max_length=50, choices=ProductType.choices, default=ProductType.other)
    image = models.ImageField(upload_to='Menproducts/', default='')
    image1 = models.ImageField(upload_to='Menproducts/', default='')
    image2 = models.ImageField(upload_to='Menproducts/', default='')

class GadgetProduct(models.Model):
    name = models.CharField(max_length=100)
    discription = models.CharField(max_length=100,default='')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    product_type = models.CharField(max_length=50, choices=ProductType.choices, default=ProductType.other)
    image = models.ImageField(upload_to='Menproducts/', default='')
    image1 = models.ImageField(upload_to='Menproducts/', default='')
    image2 = models.ImageField(upload_to='Menproducts/', default='')
    

class News_Letter(models.Model):
    email = models.EmailField(max_length=254)


class CartItem(models.Model):
    menproduct = models.ForeignKey(MenProduct, null = True ,blank = True, on_delete = models.CASCADE)
    womenproduct = models.ForeignKey(WomenProduct, null = True ,blank = True, on_delete = models.CASCADE)
    kidsproduct = models.ForeignKey(KidsProduct, null = True ,blank = True, on_delete = models.CASCADE)
    fashionproduct = models.ForeignKey(FashionProduct, null = True ,blank = True, on_delete = models.CASCADE)
    gadgetproduct = models.ForeignKey(GadgetProduct, null = True ,blank = True, on_delete = models.CASCADE)

    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(Register, on_delete=models.CASCADE)


class Contact(models.Model):
    fname = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    message =models.CharField(max_length=100)


class BillingAddress(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile_no = models.CharField(max_length=15)
    address = models.TextField()
    country = models.CharField(max_length=100, default='India')
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.address}"
