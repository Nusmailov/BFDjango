from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from main.serializers import *
from main.models import *


@api_view(['GET',  'PUT'])
def city_list(request):
    if request.method == 'GET':
        cities = City.objects.all()
        serializer = CityModelSerializer(cities, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CityModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'PUT', 'DELETE'])
def city_detail(request, pk):
    try:
        city = City.objects.get(id=pk)
    except City.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CityModelSerializer(city)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CityModelSerializer(instance=city, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        city.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

