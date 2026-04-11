from django.contrib import admin
from .models import internship_placement

@admin.register(internship_placement)
class InternshipPlacementAdmin(admin.ModelAdmin):
    list_display = ('students', 'organization_name', 'start_date', 'end_date', 'is_active')
    search_fields = ('students__username', 'organization_name')



# Register your models here.
