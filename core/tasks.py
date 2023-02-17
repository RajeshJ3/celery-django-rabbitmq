from celery import shared_task
from time import sleep

@shared_task
def my_task():
    print("[START]")
    sleep(3)
    print("[DONE]")
