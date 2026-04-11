from django.contrib import admin
from .models import InternshipPlacement

@admin.register(InternshipPlacement)
class InternshipPlacementAdmin(admin.ModelAdmin):
    list_display = ('students', 'organization_name', 'start_date', 'end_date', 'is_active')
    search_fields = ('organization_name', 'students__username')



# Register your models here.
