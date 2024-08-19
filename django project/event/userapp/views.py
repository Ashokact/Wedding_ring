from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from .forms import ProfileForm
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError

@login_required
def create_profile(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST)
        if profile_form.is_valid():
            try:
                profile = Profile.objects.get(user=request.user)
                profile_form = ProfileForm(request.POST, instance=profile)
                profile_form.save()
            except Profile.DoesNotExist:
                profile = profile_form.save(commit=False)
                profile.user = request.user
                profile.save()
            except IntegrityError:
                    return render(request, 'profile/create.html', {
                    'profile_form': profile_form,
                    'error': 'A profile already exists for this user.'
                })
            return redirect(reverse('create_profile'))
    else:
        try:
            profile = Profile.objects.get(user=request.user)
            profile_form = ProfileForm(instance=profile)
        except Profile.DoesNotExist:
            profile_form = ProfileForm()
    
    return render(request, 'profile/create.html', {'profile_form': profile_form})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user) 
            messages.info(request, "Login successful")
            return redirect('/')
        else:
            messages.info(request, "Invalid username or password")
            return redirect('login') 
        
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect(reverse('home'))

def crwelogout(request):
    auth.logout(request)
    return redirect(reverse('crew_home'))

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = auth.authenticate(username=username, password=raw_password)
            if user is not None:
                auth.login(request, user)
                return redirect(reverse('create_profile'))
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


