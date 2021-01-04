from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='list'),
    path('movie_details/<str:pk>/',views.movieDetails,name='movie_details')
]