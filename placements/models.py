from django.db import models
from django.conf import settings


# Create your models here.
class internship_placement(models.Model):
    students = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASADE,
        limit_choices_to= {'role': 'student'},
        related_name= 'placement'
    )

#company details 
organization_name = models.CharField(max_length=255)
location = models.CharField(max_length=255) 

#work place supervisor details
workplace_supervisor_name = models.CharField(max_length=255)    
workplace_supervisor_contsct = models.CharField(max_length=255) 

#duration of the placement
start_date = models.DateField()
end_date = models.DateField()

#status of the placement
is_active = models.BooleanField(default=True)

def __str__(self):
    return f"{self.students.username} - {self.organization_name}"