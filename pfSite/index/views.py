from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index/home.html')

def ability(request):
    return render(request, 'index/ability.html')

def profile(request):
    return render(request, 'index/profile.html')

def contact(request):
    return render(request, 'index/contact.html')
