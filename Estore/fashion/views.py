from django.shortcuts import render, redirect
from rest_framework import generics
from .serializers import RegisterSerializers
from rest_framework.renderers import TemplateHTMLRenderer
from django.contrib import messages
from rest_framework.response import Response
from rest_framework import status

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



class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializers

    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializers(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return render(request, 'login.html', {'user': user})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)