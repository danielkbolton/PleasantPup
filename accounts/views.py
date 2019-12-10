from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from pleasantPup_app.forms import Profile
from pleasantPup_app.forms import ProfPicForm

# Create your views here.

def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username_form = request.POST['username']
        email_form = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username_form).exists():
                context = {'error': 'Username is already taken.'}
                return render(request, 'register.html', context)
            else:
                if User.objects.filter(email=email_form).exists():
                    context = {'error':'That email already exists.'}
                    return render(request, 'register.html', context)
                else: 
                    user = User.objects.create_user(
                    username=username_form, 
                    email=email_form, 
                    password=password, 
                    first_name=first_name, 
                    last_name=last_name,
                    )
                    user.save()
                    return redirect('login')
        else:
            context = {'error':'Passwords do not match'}
            return render(request, 'register.html', context)
    else:
        return render(request, 'register.html')



def login(request):
    if request.method == "POST":
        username_form = request.POST['username']
        password_form = request.POST['password']
        user = auth.authenticate(username = username_form, password=password_form)

        if user is not None:
            auth.login(request, user)
            return redirect('profile')
        else:
            context = {'error': 'Invalid Credentials'}
            return render(request, 'login.html', context)
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('landing')


@login_required
def profile(request):
    user = request.user
    username = user.username
    if request.method == 'POST':
        form = ProfPicForm(request.POST)
        if form.is_valid():
            profile = Profile.objects.create(user_id = user.id, image_link = request.POST['image_link'])
            return redirect('profile')
    else:
        form = ProfPicForm()
        context = {'user': user, 'username': username, 'form': form, }
        if Profile.objects.filter(user_id=user.id).exists():
            profile = Profile.objects.get(user_id=user.id)
            prof_pic_link = profile.image_link    
            context['prof_pic_link'] = prof_pic_link
    return render(request, 'profile.html', context)


@login_required
def prof_pic_edit(request):
    user = request.user
    username = user.username
    profile = Profile.objects.get(user_id=user.id)
    prof_pic_link = profile.image_link    

    if request.method == 'POST':
        form = ProfPicForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save()
            return redirect('profile')
    else:
        profile.image_link = ''
        profile.save()
        form = ProfPicForm()
    context = {'user': user, 'username': username, 'form': form, 'prof_pic_link': prof_pic_link}
    return render(request, 'profile.html', context)