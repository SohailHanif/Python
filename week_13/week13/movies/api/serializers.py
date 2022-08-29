# Import serialier from Django Rest Framework
from rest_framework.serializers import ModelSerializer

# Import movie model
from movies.models import Movie

# Create serializer to convert Movie model into JSON
class MovieSerializer(ModelSerializer):
    class Meta:
        # Define model
        model = Movie
        # Define attributes to serialize
        fields = '__all__'
