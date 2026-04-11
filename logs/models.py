from django.db import models
from django.conf import settings


class daily_log(models.Model):

    #link the log to user(student)
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={'role' : 'student'}
    )


    date = models.DateField()
    tasks_performed = models.TextField()
    lessons_learned = models.TextField()
    challenges_faced =  models.TextField()

    #supervisor actions
    is_varified = models.BooleanField(default=False)    
    supervisor_comments = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f" {self.student.username} - {self.date}"
    



