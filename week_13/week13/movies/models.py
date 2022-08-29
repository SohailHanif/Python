from pyexpat import model
from django.db import models

# Import user model
from django.contrib.auth.models import User
# Import model validators
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

# Create Movie model
class Movie(models.Model):
    # Attribute to store movie name as charfield
    name = models.CharField(max_length=200)
    # Attribute to store movie description as text allowing null and blank
    description = models.TextField(null=True, blank=True)

    # Attribute to store movie year as positive int
    year = models.PositiveIntegerField()
    # Attribute to store rating as int, use validators for min and max values
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)])
    # Store user that posed the movie, set null if user deleted
    posted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    # Attribute to store when movie was last updated, automatically updates time when changed
    updated_at = models.DateTimeField(auto_now=True)
    # Attribute to store when movie was created, update only once when created
    created_at = models.DateTimeField(auto_now_add=True)

    # Override string representation of object
    def __str__(self):
        # Return movie name when printing movie model
        return self.name

# Create review model
class Review(models.Model):
    # Store movie as foreign key. if movie is deleted, review will also be deleted
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    # Store user as foreign key. if user is deleted, review will also be deleted
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Attribute to store movie review as text
    review = models.TextField(max_length=100000)
    # Attribute to store user movie rating as int
    rating = models.PositiveIntegerField( models.PositiveIntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)]))

    # If print review, will print user that created revuew
    def __str__(self):
        return f"{self.user.username}: {self.review}"
