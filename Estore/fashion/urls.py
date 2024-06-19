from django.urls import path 
from fashion import views 
from .views import RegisterView, LoginView

urlpatterns = [   
    path('', views.index,name="index"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('contact/', views.contact, name="contact"),
    path('my_account/', views.my_account, name="my_account"),
    path('product_detail/', views.product_detail, name="product_detail"),
    path('product_list/', views.product_list, name="product_list"),
    path('wishlist/', views.wishlist, name="wishlist"),
    path('reset_password/', views.Reset_password, name="reset_password"),
    path('forgot/', views.Forgot, name="Forgot"),
    path('otp/', views.OTP, name="otp"),


    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name="login"),

]