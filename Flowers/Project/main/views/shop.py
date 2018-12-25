from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from main.serializers import ShopModelSerializer
from main.models import Shop
from django.shortcuts import render, redirect


def base(request):
    return render(request, 'base.html')


def regg(request):
    return render(request, 'regg.html')


@api_view(['GET', 'POST'])
def shop_list(request):
    if request.method == 'GET':
        shops = Shop.objects.all()
        serializer = ShopModelSerializer(shops, many=True)
        context = {
            'shops': shops
        }
        return render(request, 'shop.html', context)

    elif request.method == 'POST':
        serializer = ShopModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'PUT', 'DELETE'])
def shop_detail(request, pk):
    try:
        shop = Shop.objects.get(id=pk)
    except Shop.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ShopModelSerializer(shop)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ShopModelSerializer(instance=shop, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'DELETE':
        shop.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
