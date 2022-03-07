from django.shortcuts import render,redirect
from myapp.models import tasklist
from myapp.form import taskform
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required



def index(request):
    return render(request,'index.html')

@login_required
def todolist(request):
    if request.method=="POST":
        form= taskform(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.manager = request.user
            instance.save()
            messages.success(request,("Task Added Successfully!"))
        else:    
         messages.error(request,("Please write a task first!")) 
        return redirect('todolist')    
    else:    
        all_tasks = tasklist.objects.filter(manager=request.user)
        paginate = Paginator(all_tasks,10)
        page = request.GET.get('pg')        
        all_tasks= paginate.get_page(page)

        return render(request,'task.html',{'all_tasks':all_tasks})


@login_required
def delete_task(request,task_id):

   task = tasklist.objects.get(pk=task_id)
   if task.manager == request.user: 
        task.delete()
        messages.success(request,("Task Deleted Successfully!"))

   else:    
    messages.error(request,("Access Denied!")) 
   return redirect('todolist')
    


@login_required
def complete_task(request,task_id):
   task = tasklist.objects.get(pk=task_id)
   if task.manager == request.user: 
    if(task.done == False):
        task.done = True
        task.save()
    else:
        task.done = False
        task.save()

   else:    
     messages.error(request,("Access Denied!")) 
   return redirect('todolist')


@login_required
def update_task(request, task_id):
    if request.method == "POST":
        task = tasklist.objects.get(pk=task_id)
        form = taskform(request.POST or None, instance = task)
        if form.is_valid():
            form.save()

        messages.success(request,("Task Edited!"))
        return redirect('todolist')
    else: 
        task_obj = tasklist.objects.get(pk=task_id)
        return render(request, 'edit.html', {'task_obj': task_obj})

@login_required
def about(request):
    context={
        'about_text':"About Us",
    }
    return render(request,'about.html',context)

@login_required
def contact(request):
    if request.method == "POST":
        return redirect('contact')
    else:
        return render(request,'contact.html')
