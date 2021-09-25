from django.shortcuts import render
from django.http import HttpResponse


def hello(request):
    print("Hello")
    return HttpResponse("<h1>Hello world!</h1>")
