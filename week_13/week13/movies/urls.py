from django.urls import path
# Import views from current base app folder
from . import views

# Create base app urls
urlpatterns = [
    # Route for login page
    path('login/', views.loginPage, name="login"),
    # Route for login page
    path('logout/', views.logoutUser, name="logout"),
    # Route for register page
    path('register/', views.registerUser, name="register"),

    # Add path to route to movies page view function
    path('', views.movies, name="movies"),

    # Add path to route to movie page view function
    # Use id passed in url to get movie
    path('movie/<str:pk>/', views.movie, name="movie"),

    # Route to add movie using form
    path('add_movie/', views.addMovie, name="add_movie"),
    # Route to edit movie using form
    path('update_movie/<str:pk>/', views.updateMovie, name="update_movie"),
    # Route to delete movie
    path('delete_movie/<str:pk>/', views.deleteMovie, name="delete_movie"),
]