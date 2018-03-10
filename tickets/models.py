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
    name = models.CharField(max_length=50)
    patient_name = models.CharField(max_length=50)
    insurance = models.CharField(max_length=100)
    issue = models.CharField(max_length=100)
    comment = models.TextField()
    escalate_to = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now=True)
    status = models.IntegerField(choices=STATUSES, default=SUBMITTED)
    form_user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='form_user', default=1)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']
