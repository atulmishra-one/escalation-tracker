from django.db import models
from accounts.models import MyUser
# Create your models here.


class Ticket(models.Model):
    name = models.CharField(max_length=50)
    patient_name = models.CharField(max_length=50)
    insurance = models.CharField(max_length=100)
    issue = models.CharField(max_length=100)
    comment = models.TextField()
    escalate_to = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date_created']
