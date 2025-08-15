from django.http import HttpResponse
from .tasks import send_email_task

def test_celery(request):
    send_email_task.delay("devil@gmail.com") #Run in background
    return HttpResponse("Task triggered! Check Celery worker console.") 