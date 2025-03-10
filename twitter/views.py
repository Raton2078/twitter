from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html')

def need_login(request):
    return render(request, 'needlogin.html')