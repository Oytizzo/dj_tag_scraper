from django.shortcuts import render

from .tasks import add


def hello(request):
    print("Hello")
    add.delay(100, 111, 10)
    return render(request, 'search_scraper/hello.html', {})
