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
    print(task)
    message = f"You change the task status, task information here:" \
              f"'id': {task.get('id')}," \
              f"'title': {task.get('title', '')}," \
              f"'description': {task.get('description', '')}," \
              f"'execution_period': {task.get('execution_period', '')}," \
              f"'executed': {task.get('executed', '')}"
    send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)

