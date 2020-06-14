from django.db import models
from authentication.models import User


class ShopProfile(models.Model):
    user                =   models.OneToOneField(User,on_delete=models.CASCADE)
    shop_name           =   models.CharField(max_length=120,blank=False,null=False)
    address_line_1      =   models.CharField(max_length=120,blank=False,null=False)
    address_line_2      =   models.CharField(max_length=120,blank=False,null=False)
    town_city           =   models.CharField(max_length=120,blank=False,null=False)
    country             =   models.CharField(max_length=120,blank=False,null=False)
    shop_image          =   models.FileField(upload_to='shops/',null=True, verbose_name="")
    contact             =   models.CharField(max_length=120,blank=False,null=False)
    email_address       =   models.EmailField(unique=True)
    timming             =   models.CharField(max_length=120,blank=False,null=False)
    shop_details        =   models.TextField()
    active              =   models.BooleanField(default=True)





    def __str__(self):
        return self.shop_name
