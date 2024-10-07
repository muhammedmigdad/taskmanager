from django.shortcuts import render, redirect, reverse

from django.http import HttpResponseRedirect, HttpResponse

from django.contrib.auth.decorators import login_required
from staff.models import *
from django.contrib.auth import logout as auth_logout
from .forms import TaskForm
from staff.models import Staff,Task
from main.decorators import allow_manager
from main.functions import generate_form_errors



@login_required(login_url='staff:login')
def index(request):
    alltasks = Task.objects.all()
    tasks = Task.objects.filter(is_verified=False, is_complete=True)
    verifiedtasks = Task.objects.filter(is_verified=True)
    print(tasks)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manager:index')
    else:
        form = TaskForm()
    
    context= {
            'form': form,
            'tasks': tasks,
            'verifiedtasks': verifiedtasks,
            'alltasks': alltasks
        }
    
    return render(request, 'manager/index.html', context=context)



def item_verified(request, id):
    item = Task.objects.get(id=id, is_verified=False)
    item.is_verified = True
    item.save()
    
    return HttpResponseRedirect(reverse('manager:index'))



def unauthorized_access(request):
    
    return render(request, 'manager/unauthorized_access.html')



@login_required(login_url='/login')
def delete_item(request, id):
    item = Task.objects.get(id=id)
    item.delete()
    return HttpResponseRedirect(reverse('manager:index'))