from django.contrib import admin
from todo_app.models import Task
# Register your models here.

class Taskadmin(admin.ModelAdmin):
    list_display=('task','is_completed','updated_at')
    # in admin pannel it shows wheather the tasks are completed are not even 
    # we can add creted field or any field in models
    search_fields=('task',)
admin.site.register(Task,Taskadmin)