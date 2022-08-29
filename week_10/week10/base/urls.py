from django.urls import path
# Import views from current base app folder
from . import views

# Create base app urls
urlpatterns = [
    # Add path to route to base page view function
    path('base', views.base),

    # Add path to route to base page view function
    path('contact', views.contact, name="contact"),

    # Add path to route to base page view function
    path('courses', views.courses, name="courses"),

    # Add path to route to base page view function
    path('generate_image', views.generate_image, name="generate_image"),

]
