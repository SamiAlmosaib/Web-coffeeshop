from django.http import request
from django.shortcuts import render

# Create your views here.
def signin(request):
    return render(request,'accounts/signin.html')
def signup (request):
    return render(request,'accounts/signup.html')
def profile(request):
    return render(request,'accounts/profile.html')