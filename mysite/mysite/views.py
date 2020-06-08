# I have created this file

from django.http import HttpResponse


def index(request):
    return HttpResponse("hello my web")

def about(request):
    return HttpResponse("welcome to about")