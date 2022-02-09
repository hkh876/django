from rest_framework import serializers

from .models import Genre, Movie

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = (
            'id',
            'name',
        )

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = (
            'id',
            'title',
            'rating',
            'image_path',
        )

class MovieDetailSerializer(serializers.ModelSerializer):
    movie_genre = GenreSerializer(many=True)

    class Meta:
        model = Movie
        fields = (
            'id',
            'title',
            'rating',
            'image_path',
            'release_date',
            'overview',
            'movie_genre',
        )
  