from django.db import models
from django.conf import settings 
from placements.models import InternshipPlacement


class EvaluationsCriteria(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank = True)


    def __str__(self):
        return self.name
    

class Evaluations(models.Model):
    placement = models.ForeignKey(
        InternshipPlacement,
        on_delete=models.CASCADE
    )

    criteria = models.ForeignKey( 
        EvaluationsCriteria,
        on_delete=models.CASCADE
    )

#ratings out of 10
    score = models.PositiveIntegerField()
    comments = models.TextField(blank=True, null=True)  
    date_Evatuated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Evaluation for {self.placement.students.username} - {self.criteria.name}: {self.score}"
    


