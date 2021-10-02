from django.shortcuts import render
from django.views import generic

from .tasks import add
from .models import SearchItem, ScrapeRecord


# def hello(request):
#     print("Hello")
#     add.delay(100, 111, 10)
#     return render(request, 'search_scraper/hello.html', {})


class SearchListView(generic.ListView):
    # model = SearchItem
    template_name = 'search_scraper/search_list.html'

    def get_queryset(self):
        qs = SearchItem.objects.all()

        title = self.request.GET.get('title', None)
        if title:
            qs = qs.filter(title__icontains=title)

        return qs.order_by("-publish_date")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        count = SearchItem.objects.all().count()
        context.update({
            "total_count": count
        })
        return context


class ScrapeRecordListView(generic.ListView):
    model = ScrapeRecord
    # paginate_by = 20
    template_name = 'search_scraper/scrape_history.html'
