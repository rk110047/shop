from django.db import models
from authentication.models import User
from product.models import Product
from django.db.models.signals import pre_save,post_save,m2m_changed


class OrderItem(models.Model):
    item_id     =       models.AutoField(primary_key=True)
    User        =       models.ManyToManyField(User)
    product     =       models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=True)
    quantity    =       models.IntegerField(default=1)
    price       =       models.IntegerField(default=0)
    active      =       models.BooleanField(default=True)


    #
    # def __str__(self):
    #     return  self.User

# def m2m_changed_cart_recevier(sender,instance,action,*args,**kwargs):
#     if action =="post_add" or action == 'post_remove' or action =='post_clear':
#         item_price             =       instance.product_set.product_price
#         quantity               =       instance.quantity
#         price                  =       item_price*quantity
#         instance.price         =       price
#
#
#
# m2m_changed.connect(m2m_changed_cart_recevier,sender=OrderItem.product.through)


class Cart(models.Model):
    User                 =       models.OneToOneField(User,on_delete=models.CASCADE)
    product              =       models.ManyToManyField(OrderItem)
    total_items          =       models.IntegerField(null=True,blank=True)
    total_price          =       models.IntegerField(null=True,blank=True)

# def pre_save_cart_item_total(instance,sender,*args,**kwargs):
#     if created:
#         total_items          =  instance.product.all()
#         total                =   0
#         for x in total_items:
#             total            +=  x.price
#         quantity              =   0
#         for x in total_items:
#             quantity          +=  x.quantity
#         instance.total_price    =   total
#         instance.total_items    =   quantity
#     # instance.save()
#
# pre_save.connect(pre_save_cart_item_total,sender=Cart)

# def m2m_changed_cart_recevier(sender,instance,action,*args,**kwargs):
#     if action =="post_add" or action == 'post_remove' or action =='post_clear':
#         products            =   instance.product.all()
#         total=0
#         for x in products:
#             total       += x.product_price
#         instance.total     = total
#         instance.save()
#
#
# m2m_changed.connect(m2m_changed_cart_recevier,sender=Cart.product.through)
