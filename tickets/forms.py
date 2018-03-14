from django.forms.models import ModelForm
from tickets.models import Ticket
from django import forms


class NewTicketForm(ModelForm):
    class Meta:
        model = Ticket
        exclude = ('escalated', 'form_user')

    def save(self, user_id, commit=True):
        ticket = super(NewTicketForm, self).save(commit=False)
        ticket.form_user = user_id
        if commit:
            ticket.save()
        return ticket


class EditTicketForm(ModelForm):
    class Meta:
        model = Ticket
        exclude = ('escalated', 'form_user')

    def save(self, user_id, commit=True):
        ticket = super(EditTicketForm, self).save(commit=False)
        ticket.form_user = user_id
        if commit:
            ticket.save()
        return ticket


class ImportExcelForm(forms.Form):
    file = forms.FileField()
