from django.urls import path 
from fashion import views 

urlpatterns = [   
    path('', views.index,name="index"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('contact/', views.contact, name="contact"),
    path('my_account/', views.my_account, name="my_account"),
    path('product_detail/', views.product_detail, name="product_detail"),
    path('product_list/', views.product_list, name="product_list"),
    path('wishlist/', views.wishlist, name="wishlist")

]