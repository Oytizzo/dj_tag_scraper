from django.urls import path

from . import views

app_name = 'search_scraper'

urlpatterns = [
    path('', views.hello, name="hello"),
]
