from django.shortcuts import render
from django.http import HttpResponse
from .tasks import add


def hello(request):
    print("Hello")
    add.delay(100, 9, 10)
    return HttpResponse("<h1>Hello world!</h1>")
