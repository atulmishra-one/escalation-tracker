from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserCreateForm

# Create your views here.


def profile(request):
    return render(request, 'accounts/profile.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=email, password=raw_password)
            login(request, user)
            return redirect('/accounts/profile')
    else:
        form = UserCreateForm()
    return render(request, 'accounts/signup.html', {'form': form})
