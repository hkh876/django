#from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import MethodNotAllowed, ParseError

from .models import Movie
from .serializers import MovieSerializer, MovieDetailSerializer

# Create your views here.
@api_view(['GET'])
def movieView(request):
    if request.method == 'GET':
        movie = Movie.objects.all()
        serializer = MovieSerializer(movie, many=True)
    else:
        return Response(data=MethodNotAllowed.default_code, status=MethodNotAllowed.status_code)

    return Response(data=serializer.data)

@api_view(['GET'])
def movieDetailView(request, movie_id=None):
    if request.method == 'GET':
        if movie_id is None:
            return Response(data=ParseError.default_code, status=ParseError.status_code)

        movie = get_object_or_404(Movie, id=movie_id)
        serializer = MovieDetailSerializer(movie)

    else:
        return Response(data=MethodNotAllowed.default_code, status=MethodNotAllowed.status_code)

    return Response(data=serializer.data)