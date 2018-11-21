from rest_framework.views import Response
from rest_framework.decorators import APIView, api_view
from main.models import Advert
from rest_framework import status
from main.serializers import AdvertModelSerializer


class AdvertList(APIView):
    def get(self, request):
        advert = Advert.objects.all()
        serializer = AdvertModelSerializer(advert, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AdvertModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdvertDetail(APIView):

    def get_object(self, pk):
        try:
            return Advert.object.get(id=pk)
        except Advert.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        advert = self.get_object(pk)
        serializer = AdvertModelSerializer(advert)
        return Response(serializer.data)

    def put(self, request, pk):
        advert = self.get_object(pk)
        serializer = AdvertModelSerializer(instance=advert, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self,request, pk):
        advert = self.get_object(pk)
        advert.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

