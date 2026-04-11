from django.db import models
from django.conf import settings


class InternshipPlacement(models.Model):
    students = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'student'},
        related_name='placement'
    )
    organization_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    supervisor_name = models.CharField(max_length=255)
    supervisor_contact = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.students.username} - {self.organization_name}"
