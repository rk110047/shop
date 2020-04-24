from django.db import models
from billing.models import BillingProfile

ADDRESS_TYPE_CHOICES=(('BIILING','billing'),('SHIPPING','shipping'))
class Address(models.Model):


    billingprofile       =      models.ForeignKey(BillingProfile,on_delete=models.CASCADE)
    address_type         =      models.CharField(max_length=120,choices=ADDRESS_TYPE_CHOICES,default="SHIPPING")
    address_line_1       =      models.CharField(max_length=120)
    address_line_2       =      models.CharField(max_length=120,null=True,blank=True)
    city                 =      models.CharField(max_length=120)
    state                =      models.CharField(max_length=120)
    country              =      models.CharField(max_length=120,default='INDIA')
    zip_code             =      models.IntegerField()


    def __str__(self):
        return str(self.billingprofile)
