from celery import shared_task
from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail

from task.models import Task


@shared_task
def send_message(user_id, task_id):
    user = User.objects.get(id=user_id)
    subject = f'You change the status of the task, task id:{task_id}'
    task = Task.objects.filter(id=task_id).first()
    message = f"You change the task status, task information here:" \
              f"'id': {task.id}," \
              f"'title': {task.title}," \
              f"'description': {task.description}," \
              f"'execution_period': {task.execution_period}," \
              f"'is_executed': {task.is_executed}"
    send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)

