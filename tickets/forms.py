from django.forms.models import ModelForm
from tickets.models import Ticket


class NewTicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'

