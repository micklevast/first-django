from django.http import HttpResponse
from django.shortcuts import render

def myHome(req):
    return render(req,"this is vishal chauhan")

def greetMe(req):
    return HttpResponse("hey u r welcome")

def aboutUs(request):
    return HttpResponse("welcome to about us page")