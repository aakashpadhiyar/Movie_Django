from django.shortcuts import render
from requests import Response
from rest_framework import generics
from GetData.models import *
from .serializers import *


class MovieListAPIView(generics.ListAPIView):
    queryset = MoviesList.objects.all()
    serializer_class = MoviesListSerializer

    # def list(self, request):
    #     # Note the use of `get_queryset()` instead of `self.queryset`
    #     queryset = self.get_queryset()
    #     serializer = MoviesListSerializer(queryset, many=True)
    #     return Response(serializer.data)