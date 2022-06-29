from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import TaskSerializer, CreateTaskSerializer, TaskExecutionSerializer
from .models import Task
from .tasks import send_message


class TaskView(APIView):

    def get(self, request):
        books = TaskSerializer(Task.objects.all(), many=True).data
        return Response(books, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CreateTaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class TaskDetailView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        book = self.get_serializer(self.get_object(pk), many=False).data
        return Response(book, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        task = self.get_object(pk)
        task_executed = task.executed
        serializer = self.get_serializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            if task_executed != serializer.data.get('executed'):
                send_message(request, pk)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        book = self.get_object(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TaskExecutionView(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskExecutionSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise Http404

    def post(self, request, pk):
        task = self.get_object(pk)
        task_executed = task.executed
        serializer = self.get_serializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            if task_executed != serializer.data.get('executed'):
                send_message(request, pk)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)