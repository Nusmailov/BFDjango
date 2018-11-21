defrom rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login as auth_login
from main.serializers import CustomerModelSerializer


@api_view(['POST'])
@csrf_exempt
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user is None:
        return Response({'error': 'Invalid data'})
    auth_login(request.request, user)
    token, created = Token.objects.get_or_create(user=usc


@api_view(['POST'])
@csrf_exempt
def register(request):
    if request.method == 'POST':
        serializer = CustomerModelSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view([])
@csrf_exempt
def logout(request):
    request.user.auth_token.delete()
    return Response(status=status.HTTP_200_OK)




#
# def register(request):
#     form = UserCreationForm(data=request.POST or None)
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             return Response(status=status.HTTP_200_OK)
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#
# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = auth.authenticate(username=username, password=password)
#
#         if user is not None and user.is_active:
#             auth.login(request, user)
#             return Response(status=status.HTTP_200_OK)
#         else:
#             error = "invalid data"
#             return Response(status=status.HTTP_404_NOT_FOUND)
#     else:
#         return Response(status=status.HTTP_400_BAD_REQUEST)
#
#
# def logout(request):
#     auth.logout(request)
#     return Response(status=status.HTTP_423_LOCKED)


