from django.urls import path
# Import views from current base app folder
from . import views

# Create base app urls
urlpatterns = [
    # Add path to route to movies page view function
    path('', views.movies, name="movies"),

    # Add path to route to movie page view function
    # Use id passed in url to get movie
    path('movie/<str:pk>/', views.movie, name="movie")
]