from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ViewSet
from rest_framework import generics
from .models import (
    Register,
    MenProduct,
    WomenProduct,
    KidsProduct,
    FashionProduct,
    GadgetProduct,
    News_Letter,
    CartItem,
)
from .serializers import (
    RegisterSerializers,
    LoginSerializer,
    ForgotSerializer,
    OtpSerializer,
    ResetpasswordSerializer,
    EditprofileSerializer,
    NewsLetterSerializers,
    # CartSerializers,
    ContactSerializers,
 
)
from rest_framework.renderers import TemplateHTMLRenderer
from django.contrib import messages
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import EmailMessage
import random
from django.views import View


class IndexView(View):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        user = request.session.get("username")
        register_user = Register.objects.filter(username=user).first()

        cart_items_count = CartItem.objects.filter(user=register_user).count()

        return render(request, self.template_name,
        context = {
            "cart_items_count": cart_items_count,
        })



def checkout(request):
    return render(request, "checkout.html")


def product_list(request):
    return render(request, "product-list.html")


def wishlist(request):
    return render(request, "wishlist.html")


def product_detail(request, category, id):
    if category == "men":
        product = get_object_or_404(MenProduct, id=id)
    elif category == "women":
        product = get_object_or_404(WomenProduct, id=id)
    elif category == "fashion":
        product = get_object_or_404(FashionProduct, id=id)
    elif category == "gadget":
        product = get_object_or_404(GadgetProduct, id=id)
    else:
        product = get_object_or_404(KidsProduct, id=id)
    return render(request, "product-detail.html", {"product": product})



def men_product(request):
    menproducts = MenProduct.objects.all()
    return render(request, "men-product.html", {"menproducts": menproducts})


def women_product(request):
    womenproduct = WomenProduct.objects.all()
    return render(request, "women-product.html", {"womenproduct": womenproduct})


def kids_product(request):
    kidsproduct = KidsProduct.objects.all()
    return render(request, "kids-product.html", {"kidsproduct": kidsproduct})


def fashion_product(request):
    fashionproduct = FashionProduct.objects.all()
    return render(request, "fashion-product.html", {"fashionproduct": fashionproduct})


def gadget_product(request):
    gadgetproduct = GadgetProduct.objects.all()
    return render(request, "gadget-product.html", {"gadgetproduct": gadgetproduct})


def arrival_product(request):
    return render(request, "new-products.html")


class AddtoCart(generics.ListCreateAPIView):
    
    def get(self, request, product_type, product_id):
        user = request.session["username"]
        print(product_type,"product type show")
        product_model = {
            "men": MenProduct,
            "women": WomenProduct,
            "kids": KidsProduct,
            "fashion": FashionProduct,
            "gadget": GadgetProduct,
        }.get(product_type)
        
        product = get_object_or_404(product_model, id=product_id)

        register_user = Register.objects.filter(username=user).first()
        if not register_user:
            return redirect('login')

        cart_item, created = CartItem.objects.get_or_create(
            user=register_user,
            **{f"{product_type}product": product},
            defaults={"quantity": 1},
        )

        if not created:
            cart_item.quantity += 1
            cart_item.save()

        return redirect("cart")


class CartView(View):
    template_name = "cart.html"

    def get(self, request, *args, **kwargs):
        user = request.session.get("username")
        register_user = Register.objects.filter(username=user).first()

        cart_items = CartItem.objects.filter(user=register_user)
        
        cart_subtotal = 0
        for item in cart_items:
            product = None
            if item.menproduct:
                product = item.menproduct
            elif item.womenproduct:
                product = item.womenproduct
            elif item.kidsproduct:
                product = item.kidsproduct
            elif item.fashionproduct:
                product = item.fashionproduct
            elif item.gadgetproduct:
                product = item.gadgetproduct

            if product:
                item.total_price = product.price * item.quantity
                cart_subtotal += item.total_price
            else:
                item.total_price = 0 

        shipping_cost = 30
        cart_total = cart_subtotal + shipping_cost

        return render(request, self.template_name,
        context = {
            "cart_items": cart_items,
            "cart_subtotal": cart_subtotal,
            "shipping_cost": shipping_cost,
            "cart_total": cart_total,
        })
    
class RemoveCartItemView(View):
    def get(self, request, item_id):
        user = request.session.get("username")
        register_user = Register.objects.filter(username=user).first()

        cart_item = get_object_or_404(CartItem, id=item_id, user=register_user)

        cart_item.delete()

        return redirect('cart')


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializers
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "register.html"

    def get(self, request):
        if "username" in request.session:
            return redirect("index")
        serializer = RegisterSerializers()
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect("login")
        return render(request, self.template_name)


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "login.html"

    def get(self, request, *args, **kwargs):
        if "username" in request.session:
            return redirect("index")
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.data.get("username")
            request.session["username"] = user
            return redirect("index")
        messages.error(request, serializer.errors["non_field_errors"][0])
        return render(request, self.template_name, {"serializer": serializer})



class LogoutView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        if "username" in request.session:
            del request.session["username"]
        return redirect("index")



class ForgotView(generics.CreateAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "forgot.html"
    serializer_class = ForgotSerializer

    def get(self, request):
        if "username" in request.session:
            return redirect("index")
        return render(request, self.template_name)

    def post(self, request):
        serializer = ForgotSerializer(data=request.data)
        if not serializer.is_valid():
            return redirect("forgot")
        email = serializer.data["email"]
        otp = str(random.randint(1000, 9999))
        request.session["email"] = email
        request.session["otp"] = otp
        email_subject = "Reset Password"
        email_body = f"Your OTP code is: {otp}"
        email = EmailMessage(email_subject, email_body, to=[email])
        email.send()
        return redirect("otp")



class OtpView(generics.CreateAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "otp.html"
    serializer_class = OtpSerializer

    def get(self, request):
        if "username" in request.session:
            return redirect("index")
        return render(request, self.template_name)

    def post(self, request):
        otp = request.session.get("otp")
        serializer = OtpSerializer(data=request.data, context={"otp": otp})
        if not serializer.is_valid():
            messages.error(request, serializer.errors["non_field_errors"][0])
            return redirect("otp")
        return redirect("reset_password")


class ResetpasswordView(generics.CreateAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "reset_password.html"
    serializer_class = ResetpasswordSerializer

    def get(self, request):
        if "username" in request.session:
            return redirect("index")
        return render(request, self.template_name)

    def post(self, request):
        email = request.session.get("email")
        serializer = ResetpasswordSerializer(
            data=request.data, context={"email_id": email}
        )
        if not serializer.is_valid():
            messages.error(request, serializer.errors["non_field_errors"][0])
            return redirect("reset_password")
        return redirect("login")


class ProfileView(generics.CreateAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "my-account.html"

    def get(self, request):
        if "username" not in request.session:
            return redirect("login")
        username = request.session.get("username")
        person_details = Register.objects.filter(username=username)
        return render(request, self.template_name, context={"details": person_details})


# class EditprofileView(generics.CreateAPIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = "editprofile.html"
#     serializer_class = EditprofileSerializer

#     def get(self, request):
#         if "username" not in request.session:
#             return redirect("login")
#         username = request.session.get("username")
#         person_details = Register.objects.filter(username=username)
#         return render(
#             request, self.template_name, context={"person_details": person_details}
#         )

#     def post(self, request):
#         username = request.session.get("username")
#         serializer = EditprofileSerializer(
#             data=request.data, context={"user_id": username}
#         )
#         if serializer.is_valid():
#             return redirect("profile")
#         messages.error(request, serializer.errors["non_field_errors"][0])
#         return redirect("edit")


class NewsLetterView(generics.CreateAPIView):
    serializer_class = NewsLetterSerializers
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "index.html"

    def get(self, request):
        if "username" in request.session:
            return redirect("index")
        serializer = NewsLetterSerializers()
        return render(request, self.template_name, {"serializer": serializer})

    def post(self, request, *args, **kwargs):
        serializer = NewsLetterSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect("index")
        return render(request, self.template_name)
    

class ContactView(generics.CreateAPIView):
    serializer_class = ContactSerializers
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "contact.html"

    def get(self, request):
        if "username" not in request.session:
            return redirect("login")
        serializer = ContactSerializers()
        return render(request, self.template_name, {"serializer": serializer})

    def post(self, request, *args, **kwargs):
        serializer = ContactSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect("index")
        return render(request, self.template_name)
    
# class BillingView(generics.CreateAPIView):
#     serializer_class = BillingSerializers
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = "checkout.html"

#     def get(self, request):
#         if "username" in request.session:
#             return redirect("index")
#         serializer = BillingSerializers()
#         return render(request, self.template_name)

#     def post(self, request, *args, **kwargs):
#         serializer = BillingSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return redirect("")
#         return render(request, self.template_name)
