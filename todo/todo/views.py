from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from todo import models
from todo.models import TODO
from django.contrib.auth import authenticate, logout
from django.contrib.auth import logout as lgout
from django.contrib.auth import login as lgin
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method=='POST':
        fnm = request.POST.get('fnm')
        emailid = request.POST.get('emailid')
        pwd = request.POST.get('pwd')
        print(fnm, emailid, pwd)
        user = User.objects.create_user(fnm, emailid, pwd)
        user.save()
        return redirect('/login')

    return render(request, 'register.html')

def login(request):
    if request.method=='POST':
        fnm = request.POST.get('fnm')
        pwd = request.POST.get('pwd')
        print(fnm, pwd)
        user = authenticate(request, username=fnm, password=pwd)
        if user is not None:
            lgin(request, user)
            return redirect('/todo')
        else:
            return redirect('/login')
        
    return render(request, 'login.html')

@login_required(login_url='/login')
def todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        print(title)
        obj = models.TODO(title=title, user=request.user)
        obj.save()
        user=request.user
        res=models.TODO.objects.filter(user=user).order_by('-date')
        return redirect('/todo', {'res':res})

    res=models.TODO.objects.filter(user=request.user).order_by('-date')
    return render(request, 'todo.html',{'res':res})

def logout(request):
    lgout(request)
    return redirect('/login')

@login_required(login_url='/login')
def edit_todo(request, srno):
    if request.method == 'POST':
        title = request.POST.get('title')
        print(title)
        obj = models.TODO.objects.get(srno=srno)
        obj.title=title
        obj.save()
        return redirect('/todo')

    obj=models.TODO.objects.get(srno=srno)
    return render(request, 'edit_todo.html',{'obj':obj})

@login_required(login_url='/login')
def delete_todo(request, srno):
    obj = models.TODO.objects.get(srno=srno)
    obj.delete()
    return redirect('/todo')