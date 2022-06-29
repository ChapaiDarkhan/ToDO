from task.views import TaskView, TaskDetailView, TaskExecutionView
from django.urls import path

urlpatterns = [
    path("task/", TaskView.as_view()),
    path("task/<int:pk>/", TaskDetailView.as_view()),
    path("task/<int:pk>/execute/", TaskExecutionView.as_view()),
    ]
