from rest_framework.views import Response
from rest_framework.decorators import APIView, api_view
from rest_framework.authentication import authenticate
from rest_framework.authtoken.models import Token


@api_view(['GET', 'POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user is None:
        return Response({'error': 'INVALID Data'})
    token, created = Token.objects.get_or_create(user=user)
    return Response({'token': token.key})
