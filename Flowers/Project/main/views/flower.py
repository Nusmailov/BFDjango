from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from main.serializers import FlowerModelSerializer
from main.models import Flower
from django.shortcuts import render


@api_view(['GET', 'POST'])
def flower_list(request):
    if request.method == 'GET':
        flowers = Flower.objects.all()
        serializer = FlowerModelSerializer(flowers, many=True)
        context = {
            'flowers': flowers
        }
        return render(request, 'flower.html', context)

    elif request.method == 'POST':
        serializer = FlowerModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return render(request, 'flower.html')
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'PUT', 'DELETE'])
def flower_detail(request, pk):
    try:
        flower = Flower.objects.get(id=pk)
    except Flower.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FlowerModelSerializer(flower)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = FlowerModelSerializer(instance=flower, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'DELETE':
        flower.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
