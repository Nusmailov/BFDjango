from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from main.serializers import ShopFlowerModelSerializer
from main.models import ShopFlower
from django.shortcuts import render


@api_view(['GET', 'POST'])
def shopflower_list(request):
    if request.method == 'GET':
        shopflowers = ShopFlower.objects.all()
        serializer = ShopFlowerModelSerializer(shopflowers, many=True)
        return render(request, 'base.html')
    elif request.method == 'POST':
        serializer = ShopFlowerModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'PUT', 'DELETE'])
def shopflower_detail(request, pk):
    try:
        shopflowers = ShopFlower.objects.get(id=pk)
    except ShopFlower.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ShopFlowerModelSerializer(shopflowers)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ShopFlowerModelSerializer(instance=shopflowers, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'DELETE':
        shopflowers.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
