# Create your tasks here
from time import sleep

from celery import shared_task


@shared_task
def add(x, y, sec):
    sleep(sec)
    return x + y
