from django.db import models
from django.conf import settings


# Create your models here.
class internship_placement(models.model)
    students = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASADE,
        limit_choices_to= {'role': 'student'}
    )
