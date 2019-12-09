from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers 
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from .forms import DogForm
from .models import Profile, Post, Comment, Breed, Dog


# Create your views here.




def landing(request):
    return render(request, 'landing.html')

def about(request):
    return render(request, 'about.html')

def training(request):
    return render(request, 'training.html')

""" def home(request):
    return render(request, 'home.html') """




########## DOG PROFILE ##########
@csrf_exempt
def dog_profile(request, dog_pk):
    dog = Dog.objects.get(id=dog_pk)
    context = {'dog':dog}
    return render(request, 'dog_profile.html',context)




########## EDIT DOG ##########

@login_required
def dog_create(request):
    if request.method == 'POST':
        form = DogForm(request.POST)
        if form.is_valid():
            dog = form.save(commit=False)
            dog.owner = request.user
            dog.save()
            return redirect('profile')
    else:
        form = DogForm()
    context = {'form': form, 'header': 'Add New Dog'}
    return render(request, 'dog_form.html', context)


@login_required
def dog_edit(request, dog_pk):
    dog = Dog.objects.get(id=dog_pk)
    owner = request.user
    if request.method == 'POST':
        form = DogForm(request.POST, instance=dog)
        if form.is_valid():
            dog = form.save()
            return redirect('profile')
    else:
        form = DogForm(instance=dog)
    context = {'header': f"Edit {dog.name}'s info", "dog":dog,'form': form}
    return render(request, 'dog_form.html', context)





@login_required
def dog_delete(request, dog_pk):
    dog= Dog.objects.get(id=dog_pk)
    dog.delete()
    return redirect('profile')




""" TRAINING VIEWS """

def name(request):
    return render(request, 'name.html')

def sit(request):
    return render(request, 'sit.html')

def sit2(request):
    return render(request, 'sit2.html')

def sit3(request):
    return render(request, 'sit3.html')


def down(request):
    return render(request, 'down.html')

def stand(request):
    return render(request, 'stand.html')

def stay(request):
    return render(request, 'stay.html')

def settle(request):
    return render(request, 'settle.html')

def come(request):
    return render(request, 'come.html')


