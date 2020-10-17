from django.urls import path
from .views import *
from rest_framework.authtoken import views

app_name = 'api'

urlpatterns = [
    path('MoviesListJson', MovieListAPIView.as_view(), name='UserProfileAPIView'),
]