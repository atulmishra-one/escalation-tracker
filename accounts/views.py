from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserCreateForm
from tickets.models import Ticket

# Create your views here.


def profile(request):

    submitted = Ticket.objects.filter(form_user=request.user.id, status=3).all()
    pending = Ticket.objects.filter(escalate_to=request.user.id, status=1).all()
    closed = Ticket.objects.filter(escalate_to=request.user.id, status=2).all()

    if request.user.is_manager:
        pending = Ticket.objects.filter(escalate_to=request.user.id, status=3).all()
        closed = Ticket.objects.filter(form_user=request.user.id, status=2).all()
    counts = {
        'submitted': len(submitted),
        'pending': len(pending),
        'closed': len(closed)
    }
    return render(request, 'accounts/profile.html', {'counts': counts})


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
