from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    return render(request, 'home.html')

def batman(request):
    return render(request, 'batman.html')

def joker(request):
    return render(request, 'joker.html')

def heroes(request):
    return render(request, 'heroes.html')

def villains(request):
    return render(request, 'villains.html')
