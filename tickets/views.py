from django.shortcuts import render, redirect, get_object_or_404
from tickets.forms import NewTicketForm, EditTicketForm, ImportExcelForm
from django.contrib import messages
from tickets.models import Ticket
from accounts.models import MyUser

from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.db.models import Q
from bulk_update.helper import bulk_update

# Create your views here.


@login_required
def new_ticket(request):

    if request.method == 'POST':
        form = NewTicketForm(request.POST)
        if form.is_valid():
            user = MyUser.objects.get(pk=request.user.id)
            saved_ticket = form.save(user_id=user)

            ticket = Ticket.objects.get(pk=saved_ticket.pk)
            escalate_to = ticket.escalate_to
            send_mail(
                'Escalation Mail',
                'A new ticket has been escalated to you. from {}'.format(
                    request.user
                ),
                request.user.email,
                [str(escalate_to)]
            )
            messages.success(request, 'Ticket submission successful')
            return redirect('/tickets/list/')

    else:
        form = NewTicketForm()
    return render(request, 'tickets/new.html', {'form': form})


@login_required
def edit_ticket(request, id):
    obj = get_object_or_404(Ticket, pk=id)

    if request.method == 'POST':
        form = EditTicketForm(request.POST, instance=obj)
        if form.is_valid():
            user = MyUser.objects.get(pk=request.user.id)
            form.save(user_id=user)
            messages.success(request, 'Ticket submission successful')
            return redirect('/tickets/list/')

    else:
        form = EditTicketForm(instance=obj)
    return render(request, 'tickets/edit.html', {'form': form})


@login_required
def ticket_list(request):
    statuses = Ticket.STATUSES
    # if not request.user.is_manager:
    #     # Normal User
    #     tickets = Ticket.objects.filter(
    #         form_user=request.user.id).all()
    # elif request.user.is_manager:
        # Q(form_user=request.user.id) | Q(escalate_to=request.user.id
    tickets = Ticket.objects.filter(Q(form_user=request.user.id) | Q(escalate_to=request.user.id)).all()

    status_display = 'ALL'
    if request.GET.get('filter'):
        tickets = Ticket.objects.filter(statuses=request.GET['filter'], form_user=request.user.id).all()

        filters = request.GET['filter']
        _, status = statuses[int(filters) - 1]
        if request.user.is_manager:
            if request.GET['filter'] == '1':
                tickets = Ticket.objects.filter(statuses=3, escalate_to=request.user.id).all()
                status = 'Pending'
        else:
            tickets = Ticket.objects.filter(statuses=request.GET['filter'], form_user=request.user.id).all()
            if request.GET['filter'] == '1':
                tickets = Ticket.objects.filter(statuses=1, escalate_to=request.user.id).all()
                status = 'Pending'

            if request.GET['filter'] == '2':
                tickets = Ticket.objects.filter(statuses=2, escalate_to=request.user.id).all()

        status_display = status

    return render(request, 'tickets/list.html', {'tickets': tickets, 'status_display': status_display})


@login_required
def delete_ticket(request):
    if request.method == 'POST':
        item_id = int(request.POST['delete_id'])
        item = Ticket.objects.get(pk=item_id)
        item.delete()
        return redirect('/tickets/list/')


@login_required
def import_excel(request):
    if request.method == 'POST':
        form = ImportExcelForm(request.POST, request.FILES)

        if form.is_valid():
            file_handle = request.FILES['file']
            file_handle.save_to_database(
                model=Ticket,
                initializer=None,
                mapdict={
                    'DATE': 'date_created',
                    'CLINIC': 'clinic',
                    'AGING/BATCH': 'aging_batch',
                    'ACCOUNT': 'account',
                    'PAT NAME': 'patient_name',
                    'INSURANCE NAME': 'insurance',
                    'DOS': 'dos',
                    'CPT CODES': 'cpt_codes',
                    'BILLED AMOUNT': 'billed_amount',
                    'BALANCE AMOUNT': 'balance_amount',
                    'STATUS': 'status',
                    'NOTES': 'comment',
                    'ACTION': 'action',
                    'User Name': 'escalate_to',
                    'PREVENTIVE ACTION': 'preventive_action',
                    'Worked': 'worked'
                }
            )
            count = len(file_handle.get_records())
            tickets = Ticket.objects.order_by('-id').all()[:count]
            for ticket in tickets:
                ticket.form_user = request.user
                escalate_to = ticket.escalate_to
                send_mail(
                    'Escalation Mail',
                    'A new ticket has been escalated to you. from {}'.format(
                        request.user
                    ),
                    request.user.email,
                    [str(escalate_to)]
                )
            bulk_update(tickets)

    else:
        form = ImportExcelForm()
    return render(request, 'tickets/import.html', {'form': form})
