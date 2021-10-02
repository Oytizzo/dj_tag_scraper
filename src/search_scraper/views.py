# from django.shortcuts import render
# from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# from django.shortcuts import reverse
from django.views import generic

from .models import SearchItem, ScrapeRecord
# from .forms import ScrapeForm
# from .tasks import add, task_scrape_dev_dot_to

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


# class ScrapeRecordFormView(generic.FormView):
#     template_name = 'search_scraper/scrape_history_form.html'
#     form_class = ScrapeForm
#     # success_url = '/'
#
#     def get_success_url(self):
#         return reverse("search_scraper:history")
#
#     def form_valid(self, form):
#         # try to get this url from the form
#         url = "https://dev.to/search?q=django"
#         task_scrape_dev_dot_to.delay(url)
#         return super().form_valid(form)
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         page = self.request.GET.get('page', 1)
#         qs = ScrapeRecord.objects.all()
#         paginator = Paginator(qs, 20)
#         try:
#             qs = paginator.page(page)
#         except PageNotAnInteger:
#             qs = paginator.page(1)
#         except EmptyPage:
#             qs = paginator.page(paginator.num_pages)
#         context.update({
#             "object_list": qs
#         })
#         return context
