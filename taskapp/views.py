from django.shortcuts import render

import email
from multiprocessing import context
from django.forms import Form
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from taskapp.forms import RegisterForm
#handle all the status code responses.

def index(request):
    return render(request,'index.html')

def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('login')
        
    else:    
        form = RegisterForm()
    return render(request,'registration/signup.html',{'form':form})

def logout(request):
    logout(request)
    messages.success(request,'You have successfully logged out!')
    return redirect('index')

