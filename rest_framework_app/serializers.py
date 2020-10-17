from GetData.models import  MoviesList
from rest_framework import serializers


class MoviesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoviesList
        fields = '__all__'

        # b02a447cee936a3dc622050507d952c28b499e84