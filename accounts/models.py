from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    emp_code = models.CharField(max_length=50, default=None)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.user_id.first_name

