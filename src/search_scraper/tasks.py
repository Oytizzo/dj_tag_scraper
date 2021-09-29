from time import sleep
from celery import shared_task

from .scrapers import scrape_dev_dot_to


@shared_task
def add(x, y, sec):
    sleep(sec)
    return x + y


@shared_task
def task_scrape_dev_dot_to():
    url = "https://dev.to/search?q=django"
    scrape_dev_dot_to(url)
    return
