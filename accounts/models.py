from django.contrib.auth.models import AbstractUser
from django.db import models



# Create your models here.
class CustomUser(AbstractUser):
    Role_choicrs = (
        ('student', 'student'),
        ('Accademic_supervisor', 'Accademic_supervisor'),
        ('Workplace_supervisor', 'Workplace_supervisor'),
        ('Admin', 'Administrator')
        )
    
    role = models.CharField(max_length=20, choices=Role_choicrs, default = 'student')
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    
