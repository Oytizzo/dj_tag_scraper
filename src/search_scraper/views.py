from django.shortcuts import render
from django.views import generic

from .tasks import add
from .models import SearchItem


def hello(request):
    print("Hello")
    add.delay(100, 111, 10)
    return render(request, 'search_scraper/hello.html', {})


class SearchListView(generic.ListView):
    model = SearchItem
    template_name = 'search_scraper/search_list.html'
