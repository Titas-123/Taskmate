from django.shortcuts import render,redirect
from .forms import RegForm
from django.contrib import messages



def register(request):

        if request.method== "POST":
            regform = RegForm(request.POST)
            if regform.is_valid():
                regform.save()
                messages.success(request,"Registration done successfully")
                return redirect('todolist')
        else:
            regform = RegForm()
        return render(request,'register.html',{'regform':regform})
