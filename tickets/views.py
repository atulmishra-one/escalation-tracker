from django.shortcuts import render, redirect
from tickets.forms import NewTicketForm
from django.contrib import messages
from tickets.models import Ticket

# Create your views here.


def new_ticket(request):

    if request.method == 'POST':
        form = NewTicketForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ticket submission successful')
            return redirect('/tickets/list/')

    else:
        form = NewTicketForm()
    return render(request, 'tickets/new.html', {'form': form})


def ticket_list(request):
    tickets = Ticket.objects.all()
    return render(request, 'tickets/list.html', {'tickets': tickets})

