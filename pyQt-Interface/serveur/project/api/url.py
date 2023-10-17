from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from django.conf.urls import include
from .views import UserRegistrationView, UserAuthenticationView,Dht11ViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Dht11',Dht11ViewSet)


urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('login/', UserAuthenticationView.as_view(), name='user-authentication'),
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
    path('',include(router.urls))
]
