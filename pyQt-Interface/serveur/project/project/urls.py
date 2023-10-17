
from django.contrib import admin
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from api.views import UserRegistrationView, UserAuthenticationView
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('login/', UserAuthenticationView.as_view(), name='user-authentication'),
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
    path('api/',include('api.url'))
    
]


