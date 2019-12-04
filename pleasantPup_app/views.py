from django.shortcuts import render, redirect

# Create your views here.




def landing(request):
    return render(request, 'landing.html')

def about(request):
    return render(request, 'about.html')

""" def home(request):
    return render(request, 'home.html') """
