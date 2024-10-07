from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from staff.models import Staff,Task

from django.shortcuts import redirect


@login_required(login_url='/login')
def index(request):
    user = request.user
    staff = Staff.objects.get(user=user)
    tasks = Task.objects.filter(staff=staff, is_complete=False)
    donetasks = Task.objects.filter(staff=staff, is_complete=True)

    context = {
        'tasks': tasks,
        'donetasks': donetasks,
        'user': user,
        'staff': staff,
    }
    return render(request, 'web/index.html', context=context)


def login(request):
    error_message = None
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        
        user = authenticate(request, username=username, password=password)
    
        if user is not None:
            auth_login(request, user)
            return HttpResponseRedirect(reverse('staff:index'))
        else:
            
            error_message = 'Invalid name or pass.'
    
    return render(request, 'web/login.html', {'error_message': error_message})

    

def logout(request):
    auth_logout(request)

    return HttpResponseRedirect(reverse('staff:login'))


@login_required(login_url='/login')
def item_done(request, id):
    item = Task.objects.get(id=id, is_complete=False)
    item.is_complete = True
    item.save()
    
    return HttpResponseRedirect(reverse('staff:index'))


@login_required(login_url='/login')
def delete_item(request, id):
    item = Task.objects.get(id=id)
    item.delete()
    return HttpResponseRedirect(reverse('staff:index'))