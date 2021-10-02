from django.urls import path

from . import views

app_name = 'search_scraper'

urlpatterns = [
    # path('', views.hello, name="hello"),
    path('scrape_list/', views.SearchListView.as_view(), name="search-list"),
    path('history/', views.ScrapeRecordListView.as_view(), name='history'),
]
