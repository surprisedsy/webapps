from django.shortcuts import render
from emaillist.models import fetchall
# Create your views here.

def index(request) :
    results = fetchall()
    data = {"emaillist" : results}
    return render(request, 'emaillist/index.html', data)