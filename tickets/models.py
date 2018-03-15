from django.db import models
from accounts.models import MyUser
# Create your models here.


class Ticket(models.Model):
    REJECTED = 1  # Manager can this <=pending>
    CLOSED = 2  # Manager can do this
    SUBMITTED = 3  # User can do this and manager

    STATUSES = (
        (REJECTED, 'Reverted'),
        (CLOSED, 'Closed'),
        (SUBMITTED, 'Submitted')
    )
    date_created = models.CharField(max_length=20, null=True)
    clinic = models.CharField(max_length=50, null=True)
    aging_batch = models.CharField(max_length=50, null=True)
    account = models.CharField(max_length=50, null=True)
    patient_name = models.CharField(max_length=50, null=True)
    insurance = models.CharField(max_length=100, null=True)
    dos = models.CharField(max_length=255, blank=True, null=True)
    cpt_codes = models.CharField(max_length=100, null=True)
    billed_amount = models.CharField(null=True, max_length=20)
    balance_amount = models.CharField(null=True, max_length=20)
    status = models.CharField(max_length=60, null=True)
    comment = models.TextField(blank=True, null=True)
    action = models.CharField(max_length=60, null=True)
    escalate_to = models.CharField(max_length=100, null=True)
    preventive_action = models.TextField(null=True)
    worked = models.CharField(max_length=255, blank=True, null=True)
    statuses = models.IntegerField(choices=STATUSES, default=SUBMITTED)
    form_user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='form_user', default=1)

    def __str__(self):
        return self.patient_name

    class Meta:
        ordering = ['-id']
