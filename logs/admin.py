
from django.contrib import admin
from .models import daily_log, WeeklyLog


# Register your models here.
@admin.register(daily_log)
class daily_LogAdmin(admin.ModelAdmin):
    list_display = ('student' , 'date')
    list_filter = ('date', 'student')
    search_fields = ('student__username',)

@admin.register(WeeklyLog)
class WeeklyLogAdmin(admin.ModelAdmin):
    list_display = ('student' , 'week_number', 'submitted_at')
    list_filter = ('week_number',)

