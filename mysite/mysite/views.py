# I have created this file

from django.http import HttpResponse
from django.shortcuts import render

def login(request):
    # params={"name":"Nitish","place":"ahmedabad"}
    return render(request, 'login_page.html')


def signup(request):
    # params={"name":"Nitish","place":"ahmedabad"}
    return render(request, 'sign_up_page.html')

# def details(request):
#     print(request.GET.get("uname"))
#     print(request.GET.get("psw"))
#     return HttpResponse("welcome to about")