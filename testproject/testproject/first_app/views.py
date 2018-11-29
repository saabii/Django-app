# from django.shortcuts import render

from django.http import HttpResponse


# Create your views here.

#def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")

def index(reguest):
    return HttpResponse("<h3>Hi Sierj! Have a nice day!</h3>")
