from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserCreateForm
from tickets.models import Ticket

# Create your views here.


def profile(request):

    submitted = Ticket.objects.filter(form_user=request.user.id, statuses=3).all()
    pending = Ticket.objects.filter(escalate_to=request.user.email, statuses=1).all()
    closed = Ticket.objects.filter(escalate_to=request.user.email, statuses=2).all()

    if request.user.is_manager:
        pending = Ticket.objects.filter(escalate_to=request.user.email, statuses=3).all()
        closed = Ticket.objects.filter(form_user=request.user.id, statuses=2).all()

    from_date, to_date = request.GET.get('from_date'), request.GET.get('to_date')
    if from_date and to_date:
        submitted = Ticket.objects.filter(
            form_user=request.user.id, statuses=3, date_created__range=[
                from_date,
                to_date
            ]).all()
        pending = Ticket.objects.filter(
            escalate_to=request.user.email, statuses=1, date_created__range=[
                from_date,
                to_date
            ]).all()
        closed = Ticket.objects.filter(
            escalate_to=request.user.email, statuses=2, date_created__range=[
                from_date,
                to_date
            ]).all()

    counts = {
        'submitted': len(submitted),
        'pending': len(pending),
        'closed': len(closed)
    }
    return render(request, 'accounts/profile.html',
                  {'counts': counts, 'from_date': from_date, 'to_date': to_date})


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
