from django.contrib import admin

# Import models in current application folder
from .models import Movie, Review

# Register your models here.

# Register movie model in admin panel
admin.site.register(Movie)

# Register movie model in admin panel
admin.site.register(Review)
