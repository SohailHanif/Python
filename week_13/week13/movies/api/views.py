# Import decorator for api view from DRF
from rest_framework.decorators import api_view
# Import Response from DRF
from rest_framework.response import Response
from movies.models import Movie
from .serializers import MovieSerializer

# Use decorator to define allowed methods
@api_view(['GET'])
# Create api to get available routes
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/movies',
        'GET /api/movies/:id'
    ]
    # Return dict as DRF response
    return Response(routes)


@api_view(['GET'])
def getMovies(request):
    # Queryset for all movies
    movies = Movie.objects.all()
    # Serialize queryset
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


# API that accepts get requests with pk to get movie by id
@api_view(['GET'])
def getMovie(request, pk):
    # Queryset for movie with matching id
    room = Movie.objects.get(id=pk)
    # Serialize queryset
    serializer = MovieSerializer(room, many=False)
    return Response(serializer.data)
