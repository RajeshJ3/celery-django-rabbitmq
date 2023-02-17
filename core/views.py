from django.http import JsonResponse
from .tasks import my_task

def index(request, *args, **kwargs):
    my_task.delay()
    data = {"success": True}
    return JsonResponse(data)
