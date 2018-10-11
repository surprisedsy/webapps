from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from emaillist import models
# Create your views here.

def index(request) :
    results = models.fetchall()
    data = {"emaillist_list" : results}
    return render(request, 'emaillist/index.html', data)

def form(request) :
    return render(request, 'emaillist/form.html')

def add(request) :
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']

    models.insert((first_name, last_name, email))

    return HttpResponseRedirect("/emaillist")