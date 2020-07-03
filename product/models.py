from django.db import models
from shopkeeper.models import ShopProfile
from authentication.models import User

class Brand(models.Model):
    brand_name      =       models.CharField(max_length=120)
    brand_image     =       models.ImageField(null=True,blank=True)


    def __str__(self):
        return self.brand_name
    class Meta:
        # unique_together = ['album', 'order']
        ordering = ['brand_name']


class SubCategory(models.Model):
    category_name        =       models.CharField(max_length=120)
    image                =       models.FileField(upload_to='SubCategory',null=True,blank=True)

    def __str__(self):
        return self.category_name


class Categories(models.Model):
    category_name        =       models.CharField(max_length=120)
    image                =       models.ImageField(upload_to='Categories/',blank=True,null=True)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_id      =   models.AutoField(primary_key=True)
    product_code    =   models.CharField(max_length=120,null=True,blank=True)
    user            =   models.ForeignKey(User,on_delete=models.CASCADE)
    shop_name       =   models.ForeignKey(ShopProfile,on_delete=models.CASCADE)
    product_name    =   models.CharField(max_length=120,blank=False,null=False)
    product_price   =   models.DecimalField(max_digits=10,decimal_places=2)
    product_image   =   models.FileField(upload_to='product_images/', null=True, verbose_name="")
    # product_color   =   models.CharField(max_length=120)
    # product_size    =   models.CharField(max_length=120)
    # brand_name      =   models.ForeignKey(Brand,on_delete=models.SET_NULL,null=True)
    quantity        =   models.CharField(max_length=120,blank=False,null=False)
    # slug            =   models.SlugField()
    Category        =   models.ForeignKey(Categories,on_delete=models.SET_NULL,null=True)
    description     =   models.TextField()
    active          =   models.BooleanField(default=True)


    def __str__(self):
        return  self.product_name

    @property
    def owner(self):
        return self.user


class ProductItem(models.Model):
    user             =   models.ForeignKey(User,on_delete=models.CASCADE)
    Product          =   models.ForeignKey(Product,on_delete=models.CASCADE)
