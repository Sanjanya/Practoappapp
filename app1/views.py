
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm


def homepage(request):
    return render(request, 'home.html')
#change
# appname/views.py


def sign_up(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})


def loginpage(request):
    return render(request, 'login.html')
