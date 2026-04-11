from django.contrib import admin
from .models import EvaluationsCriteria, Evaluations


@admin.register(EvaluationsCriteria)
class EvaluationsCriteriaAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Evaluations)
class EvaluationsAdmin(admin.ModelAdmin):
    list_display = ('placement', 'criteria', 'score', 'date_Evatuated')
    list_filter = ('criteria', 'placement__organization_name')