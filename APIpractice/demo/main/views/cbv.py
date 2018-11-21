from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from main.serializers import TaskModelSerializer, TeacherModelSerializer
from main.models import Task, Teacher


class TaskList(APIView):
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskModelSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = TaskModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetail(APIView):

    def get_object(self, pk):
        try:
            return Task.object.get(id=pk)
        except Task.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        task = self.get_object(pk)
        serializer = TaskModelSerializer(task)
        return Response(serializer.data)

    def put(self, request, pk):
        task = self.get_object(pk)
        serializer = TaskModelSerializer(instance=task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self,request, pk):
        task = self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TeacherList(APIView):

    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherModelSerializer(teachers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TeacherModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TeacherDetail(APIView):

    def get(self, request, pk):
        teacher = Teacher.objects.get(id=pk)
        serializer = TeacherModelSerializer(teacher)
        return Response(serializer.data)

    def put(self, request, pk):
        teacher = Teacher.objects.get(id=pk)
        serializer = TeacherModelSerializer(instance=teacher, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        teacher = self.get_object(pk)
        teacher.delete()
        return Response(status.HTTP_204_NO_CONTENT)
