from main.models import Task
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from main.models import Teacher
from django.views.decorators.csrf import csrf_exempt

from main.serializers import TaskModelSerializer, UserSerializer, TaskSerializer
from main.models import Task

@api_view(['GET', 'POST'])
def tasks_list(request, format=None):
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskModelSerializer(tasks, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TaskModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, )
        return Response(serializer.errors,)


@api_view(['GET', 'POST', 'DELETE'])
def tasks_detail(request, pk):
    try:
        task = Task.objects.get(id=pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TaskModelSerializer(task)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TaskModelSerializer(instance=task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST', 'DELETE'])
def teachers_detail(request, format=None):
    if request.method == 'GET':
        teachers = Teacher.objects.all()
        serializer = Teacher