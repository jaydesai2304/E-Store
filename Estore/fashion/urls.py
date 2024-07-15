from django.urls import path
from fashion import views
from django.conf.urls.static import static
from django.conf import settings
from .views import (
    RegisterView,
    LoginView,
    OtpView,
    ForgotView,
    ProfileView,
    ResetpasswordView,
    LogoutView,
    NewsLetterView,
    AddtoCart,
    CartView,
    ContactView,
)

urlpatterns = [
    path("", views.index, name="index"),
    path("checkout/", views.checkout, name="checkout"),
    path("product_list/", views.product_list, name="product_list"),
    path("wishlist/", views.wishlist, name="wishlist"),
    path("men_product/", views.men_product, name="men_product"),
    path("women_product/", views.women_product, name="women_product"),
    path("kids_product/", views.kids_product, name="kids_product"),
    path("fashion_product/", views.fashion_product, name="fashion_product"),
    path("gadget_product/", views.gadget_product, name="gadget_product"),
    path("arrival_product/", views.arrival_product, name="arrival_product"),
    path("product/<str:category>/<int:id>/", views.product_detail, name="product_detail" ),

    path('add-to-cart/<str:product_type>/<int:product_id>/', AddtoCart.as_view(), name='add_to_cart'),

    path("cart/", CartView.as_view(), name="cart"),
    path("reset_password/", ResetpasswordView.as_view(), name="reset_password"),
    path("forgot/", ForgotView.as_view(), name="forgot"),
    path("otp/", OtpView.as_view(), name="otp"),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("newsletter/", NewsLetterView.as_view(), name="newsletter"),
    path("my_account/", ProfileView.as_view(), name="my_account"),
    path("contact/", ContactView.as_view(), name="contact"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)