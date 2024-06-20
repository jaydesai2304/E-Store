from django.shortcuts import render, redirect
from rest_framework import generics
from .serializers import RegisterSerializers, LoginSerializer, ForgotSerializer, OtpSerializer, ResetpasswordSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from django.contrib import messages
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import EmailMessage
import random

def index(request):
    return render(request, 'index.html')

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def contact(reqest):
    return render(reqest, 'contact.html')

def my_account(request):
    return render(request, "my-account.html")

def product_detail(request):
    return render(request, 'product-detail.html')

def product_list(request):
    return render(request, 'product-list.html')

def wishlist(request):
    return render(request, 'wishlist.html')

def Reset_password(request):
    return render(request, 'reset_password.html')


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
            user = serializer.save()
        return render(request, self.template_name, {'user': user})

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
            user = serializer.data.get('username')
            request.session["username"] = user
            return redirect("index")
        messages.error(request, serializer.errors["non_field_errors"][0])
        return render(request, self.template_name, {'serializer': serializer})
    
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
        email_subject = "Your OTP Code"
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