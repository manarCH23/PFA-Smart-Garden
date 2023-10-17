from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Dht11
from .serializers import UserSerializer,Dht11Serializer

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserSerializer

class UserAuthenticationView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(UserAuthenticationView, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key})


class Dht11ViewSet(viewsets.ModelViewSet):
    queryset = Dht11.objects.all()
    serializer_class = Dht11Serializer
