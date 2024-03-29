from django.db import models
from authentication.models import User
from django.db.models.signals import post_save
# Create your models here.


class BillingProfile(models.Model):
    User                =       models.OneToOneField(User,on_delete=models.CASCADE)
    email               =       models.EmailField(unique=True)
    active              =       models.BooleanField(default=True)
    timestamp           =       models.DateTimeField(auto_now_add=True)
    updated             =       models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.email


def user_created_receiver(instance,sender,created,*args,**kwargs):
    if created:
        BillingProfile.objects.get_or_create(User=instance,email=instance.email)

post_save.connect(user_created_receiver,sender=User)
