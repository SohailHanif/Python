# Import ModelForm
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
# Import movie
from .models import Movie

# Create movie form
class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
        exclude = ['posted_by', 'updated_at', 'created_at']
        