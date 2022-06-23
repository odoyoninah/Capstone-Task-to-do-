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
#handle all the status code responses.

def index(request):
    return render(request,'index.html')