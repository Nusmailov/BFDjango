from rest_framework.views import Response
from main.models import Advert
from rest_framework import status
from main.serializers import AdvertModelSerializer
from rest_framework.decorators import APIView, api_view


@api_view(['GET', 'POST'])
def advert_list(request, format=None):
    if request.method == 'GET':
        tasks = Advert.objects.all()
        serializer = AdvertModelSerializer(tasks, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AdvertModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, )
        return Response(serializer.errors,)


@api_view(['GET', 'POST', 'DELETE'])
def advert_detail(request, pk):
    try:
        task = Advert.objects.get(id=pk)
    except Advert.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AdvertModelSerializer(task)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = AdvertModelSerializer(instance=task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)