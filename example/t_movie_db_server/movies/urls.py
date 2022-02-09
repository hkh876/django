from django.urls import path
from .views import movieView, movieDetailView

urlpatterns = [
    path('', movieView, name='movieView'),
    path('<int:movie_id>', movieDetailView, name='movieDetailView')
]