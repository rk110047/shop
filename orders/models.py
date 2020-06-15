from django.db import models
from cart.models import Cart
from billing.models import BillingProfile
from addresses.models import Address
from .utils import unique_id_generator
from authentication.models import User
from django.db.models.signals import pre_save,post_save

class Order(models.Model):
    order_status_choices=(('CREATED','created'),('PAID','paid'),('SHIPPED','shipped'),('REFUNDED','refunded'))

    billing_profile =   models.ForeignKey(BillingProfile,null=True,blank=True,on_delete=models.CASCADE)
    billing_address =   models.ForeignKey(Address,related_name='billing_address',on_delete=models.CASCADE)
    shipping_address =   models.ForeignKey(Address,related_name='shipping_address',on_delete=models.CASCADE)
    order_id        =   models.CharField(max_length=120,blank=True)
    cart            =   models.ForeignKey(Cart,on_delete=models.CASCADE)
    shipping_total  =   models.DecimalField(default=0.00,decimal_places=2,max_digits=100)
    total           =   models.DecimalField(default=0.00,decimal_places=2,max_digits=100)
    order_status    =   models.CharField(max_length=120,choices=order_status_choices,default='created')
    active          =   models.BooleanField(default=True)
    ordered         =   models.BooleanField(default=False)
    User            =   models.ManyToManyField(User)

    def __str__(self):
        return self.order_id

    def update_total(self):
        cart_total          =   self.cart.total_price
        shipping_total      =   self.shipping_total
        new_total           =   cart_total+shipping_total
        self.total          =   new_total
        self.save()
        return new_total



def pre_save_order_id_creator(instance,sender,*args,**kwargs):
    if not instance.order_id:
        instance.order_id = unique_id_generator(instance)


pre_save.connect(pre_save_order_id_creator,sender=Order)


def post_save_order_total(instance,sender,created,*args,**kwargs):
    if not created:
        cart_obj        =   instance
        cart_id         =   cart_obj.id
        qs              =   Order.objects.filter(cart_id=cart_id)
        if qs.count()==1:
            order_obj   =   qs.first()
            order_obj.update_total()

post_save.connect(post_save_order_total,sender=Cart)



def post_save_order_total_saver(instance,sender,created,*args,**kwargs):
    if created:
        instance.update_total()

post_save.connect(post_save_order_total_saver,sender=Order)
