from django.db import models
from authentication.models import User


class CustomerProfile(models.Model):
    Customer_id         =    models.AutoField(primary_key=True)
    User                =    models.OneToOneField(User,on_delete=models.CASCADE)
    first_name          =    models.CharField(max_length=20)
    middle_name         =    models.CharField(max_length=20)
    last_name           =    models.CharField(max_length=20)
    email               =    models.EmailField()
    phone_number        =    models.IntegerField()
    address_line_1      =    models.CharField(max_length=120)
    address_line_2      =    models.CharField(max_length=120,null=True,blank=True)
    address_line_3      =    models.CharField(max_length=120,null=True,blank=True)
    town_city           =    models.CharField(max_length=120)
    state               =    models.CharField(max_length=120)
    country             =    models.CharField(max_length=120)
    zip_code            =    models.IntegerField()



    def __str__(self):
        return self.User
