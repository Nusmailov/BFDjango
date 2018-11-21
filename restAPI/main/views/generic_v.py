from rest_framework import generics

from main.serializers import RestaurantModelSerializer,UserSerializer
from main.models import Restaurant
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class IsSuperAdmin(IsAuthenticated):
    def has_permission(self, request, view):
        return request.user and request.user.is_superuser

class GenericRestaurantList(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantModelSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Restaurant.objects.for_user(self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class GenericRestaurantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantModelSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    lookup_field = 'restaurant_id'

    def get_object(self):
        return Restaurant.objects.get(id=self.kwargs[self.lookup_field])

    def get_queryset(self):
        return Restaurant.objects.for_user(self.request.user)
