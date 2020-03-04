from django.shortcuts import render

def home(request):
    return render(request, 'items/home.html')
