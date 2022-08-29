from pyexpat import model
from django.db import models

# Create your models here.

# Create Movie model
class Movie(models.Model):
    # Attribute to store movie name as charfield
    name = models.CharField(max_length=200)
    # Attribute to store movie description as text allowing null and blank
    description = models.TextField(null=True, blank=True)
    # Attribute to store when movie was last updated, automatically updates time when changed
    updated = models.DateTimeField(auto_now=True)
    # Attribute to store when movie was created, update only once when created
    # created = model.DateTimeField(auto_now_add=True)

    # Override string representation of object
    def __str__(self):
        # Return movie name when printing movie model
        return self.name
