from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from reg.api.views import RegisterView




urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('reg/', RegisterView.as_view(), name='register'),
]