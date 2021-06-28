from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request,'login.html')

def signup(request):
    return render(request, 'signup.html')

def forgot_password(request):
    return render(request, 'forgot_password.html')