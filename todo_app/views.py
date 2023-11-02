from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Task

def addtask(request):
    task = request.POST['task']
    # user will submit add ask in input field and that will be stored in dict 
    # and the key name[task] will be taken and col;ected in a variable called task
    Task.objects.create(task=task)
    # this will add the task created in the admin pannel
    return redirect('home')

def mark_as_done(request , pk):
    task = get_object_or_404(Task,pk=pk)
    task.is_completed = True
    # once the value is assigned to the field it should be saved 
    task.save()
    # data of completed task is saved
    return redirect('home')

def mark_as_undone(request , pk):
    task = get_object_or_404(Task,pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')

def edit_task(request,pk):
    get_task = get_object_or_404(Task,pk=pk)
    if request.method == 'POST':
        new_task = request.POST['task']
        # edited task will be collected in a variable as new task
        get_task.task = new_task
        # get task is the variable where older task name is collected
        #  now we have to update it with new task name
        get_task.save()
        return redirect('home')
    else:
        context ={
            'get_task':get_task,
        }
        # by default display the task name in edit input box 
        # so pass this varibale name get_task in the edit task html file as a value ="gettask.task"
        return render(request,'edit_task.html',context)

def delete_task(request,pk):
    task = get_object_or_404(Task,pk=pk)
    task.delete()
    return redirect('home')


