
from django.contrib import admin
from .models import daily_log


# Register your models here.
@admin.register(daily_log)
class daily_LogAdmin(admin.ModelAdmin):
    list_display = ('student' , 'date')
    list_filter = ('date', 'student')
    search_fields = ('student__username',)



def save_model(self, request, obj, form, change):
    if not change:  # Only set the student field when creating a new log
        obj.student = request.user
    super().save_model(request, obj, form, change)  
