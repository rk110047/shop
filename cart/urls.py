from django.urls import path
from .views import CartAPIView,ItemCreateAPIView,RemoveItemFromCartAPIView,CheckOutAPIView,OrderItemDeleteAPIView,getCartAPIView,orderItemCartAPIView

app_name="cart"


urlpatterns=[
    path('',CartAPIView.as_view(),name='cart'),
    path('get/<id>',getCartAPIView.as_view()),
    path('order_item/<item_id>',orderItemCartAPIView.as_view(),name="order_item"),
    path('checkout/',CheckOutAPIView.as_view(),name='cart'),
    path('add_to_cart/<product_id>/',ItemCreateAPIView.as_view(),name="add_to_cart"),
    path('remove_from_cart/<product_id>/',RemoveItemFromCartAPIView.as_view(),name="remove_from_cart"),
    path('delete_item_from_cart/<item_id>/',OrderItemDeleteAPIView.as_view(),name="delete_item_from_cart")

]
