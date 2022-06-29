from celery import shared_task
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail

from task.models import Task


@shared_task
def send_message(request, pk):
    subject = f'You change the status of the task, task id:{pk}'
    task = Task.objects.filter(id=pk).values().first()
    message = f"You change the task status, task information here:" \
              f"'id': {task.id}," \
              f"'title': {task.title}," \
              f"'description': {task.description}," \
              f"'execution_period': {task.execution_period}," \
              f"'executed': {task.executed}"
    send_mail(subject, message, settings.EMAIL_HOST_USER, [request.user.email], fail_silently=False)
    messages.success(request, 'Success!')
    return 'Task done successfully'
