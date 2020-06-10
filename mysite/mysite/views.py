# I have created this file

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params={"name":"Nitish","place":"ahmedabad"}
    return render(request, 'index.html',params)

def about(request):
    return HttpResponse("welcome to about")