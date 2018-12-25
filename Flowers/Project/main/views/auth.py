from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from main.serializers import UserModelSerializer
from django.shortcuts import render


@api_view(['GET','POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user is None:
        return render(request, 'login3.html')
    token, created = Token.objects.get_or_create(user=user)
    return Response(status=status.HTTP_200_OK)


@api_view(['GET','POST'])
def register(request):
    if request.method == 'POST':
        serializer = UserModelSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                user.set_password(raw_password=request.data.get('password'))
                user.save()
                return render(request, 'register.html')
        return render(request, 'login3.html')
    return render(request, 'login3.html')
    # form = UserModelSerializer(data=request.POST or None)
    # if request.method == 'POST':
    #     if form.is_valid():
    #         form.save()
    #         return render('base.html')
    # return render(request, 'register.html', {'form': form})


@api_view([])
def logout(request):
    request.user.auth_token.delete()
    return Response(status=status.HTTP_200_OK)
