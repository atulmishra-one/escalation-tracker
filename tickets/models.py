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
    date_created = models.DateField()
    clinic = models.CharField(max_length=50, blank=True)
    aging_batch = models.CharField(max_length=50, blank=True)
    account = models.CharField(max_length=50, blank=True)
    patient_name = models.CharField(max_length=50, blank=True)
    insurance = models.CharField(max_length=100, blank=True)
    cpt_codes = models.CharField(max_length=100, blank=True)
    billed_amount = models.IntegerField(default=0)
    balance_amount = models.IntegerField(default=0)
    statusA = models.CharField(max_length=60, blank=True)
    comment = models.TextField(blank=True)
    action = models.CharField(max_length=60)
    escalate_to = models.CharField(max_length=100, blank=True)
    preventive_action = models.TextField(blank=True)
    worked = models.CharField(max_length=255, blank=True)
    status = models.IntegerField(choices=STATUSES, default=SUBMITTED)
    form_user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='form_user', default=1)

    def __str__(self):
        return self.patient_name

    class Meta:
        ordering = ['-id']
