
from django.contrib import admin
from .models import daily_log


# Register your models here.
@admin.site.register(daily_log)
class daily_LogAdmin(admin.ModelAdmin):
    list_display = ('student' , 'date')
    list_filter = ('date', 'student')
    search_fields = ('student__username')
