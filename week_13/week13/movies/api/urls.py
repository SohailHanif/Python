# Import path
from django.urls import path
# Import api views
from . import views

# Define API routes
urlpatterns = [
    path('',  views.getRoutes),
    path('movies/', views.getMovies),
    path('movies/<str:pk>/', views.getMovie),
]
