from django.db import models
from authentication.models import User


class CustomerProfile(models.Model):
    Customer_id         =    models.AutoField(primary_key=True)
    User                =    models.OneToOneField(User,on_delete=models.CASCADE)
    profile_image       =    models.FileField(upload_to='profile_pic/',null=True)
    first_name          =    models.CharField(max_length=20)
    middle_name         =    models.CharField(max_length=20,null=True)
    last_name           =    models.CharField(max_length=20,null=True)
    email               =    models.EmailField()
    phone_number        =    models.CharField(max_length=20,null=True)
    address_line_1      =    models.CharField(max_length=120)
    town_city           =    models.CharField(max_length=120)
    state               =    models.CharField(max_length=120)
    country             =    models.CharField(max_length=120)
    zip_code            =    models.IntegerField()



    def __str__(self):
        return self.User
