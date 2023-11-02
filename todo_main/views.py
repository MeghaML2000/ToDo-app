from django.shortcuts import render
from todo_app.models import Task
# Create your views here.
def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')
    # this is to show the task added by the user on frontend
    # orderby is used to show the recently added task that is added by the user 
    completed_tasks = Task.objects.filter(is_completed=True)
    # to display completed task 

    context ={
        'tasks':tasks,
        'completed_tasks':completed_tasks,
    }
    return render(request,'home.html',context)