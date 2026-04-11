from django.db import models
from django.conf import UserSettingsHolders
from placements.models import InternshipPlacement


class EvaluationsCriteria(models.Model):
    name = Models.Charfield(max_length=100)
    description = models.TextField(blank = True)


    def __str__(self):
        return self.name
