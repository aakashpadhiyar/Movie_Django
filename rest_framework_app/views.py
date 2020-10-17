from django.shortcuts import render
from rest_framework import generics
from GetData.models import *
from .serializers import *


class MovieListAPIView(generics.ListAPIView):
    queryset = MoviesList.objects.all()
    serializer_class = MoviesListSerializer