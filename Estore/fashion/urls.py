from django.urls import path 
from fashion import views 
from django.conf.urls.static import static
from django.conf import settings
from .views import RegisterView, LoginView, OtpView, ForgotView, ResetpasswordView, LogoutView

urlpatterns = [   
    path('', views.index,name="index"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('contact/', views.contact, name="contact"),
    path('my_account/', views.my_account, name="my_account"),
    path('product_list/', views.product_list, name="product_list"),
    path('wishlist/', views.wishlist, name="wishlist"),
    path('men_product/', views.men_product, name="men_product"),
    path('women_product/', views.women_product, name="women_product"),
    path('kids_product/', views.kids_product, name="kids_product"),
    path('fashion_product/', views.fashion_product, name="fashion_product"),
    path('gadget_product/', views.gadget_product, name="gadget_product"),
    path('arrival_product/', views.arrival_product, name="arrival_product"),
    path('product/<str:category>/<int:id>/', views.product_detail, name='product_detail'),


    path('reset_password/', ResetpasswordView.as_view(), name="reset_password"),
    path('forgot/', ForgotView.as_view(), name="forgot"),
    path('otp/', OtpView.as_view(), name="otp"),
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
   

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)