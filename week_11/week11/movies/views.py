from django.shortcuts import render
# Import HTTP
from django.http import HttpResponse

# Create movie object array
movies_array = [
    {"id": 1, "name": "Monthy Python and the Holy Grail"},
    {"id": 2, "name": "The Lion King"},
    {"id": 3, "name": "Pirates of the Carribean"}
]


# Create your views here.

# View for movies
def movies(request):
    # Put page title and movies array to be passed in context
    context = {
        "page_title": "Movies",
        "movies_array": movies_array,
    }

    # Render movies template with context
    return render(request, "homepage.html", context)

# View for movie based on id get param
def movie(request, pk):
    # Create object to store movie
    movie = None
    # Search through all movies for one where id matches pk
    for movie_index in movies_array:
        # check to see if pk matches movie int
        if pk == str(movie_index.get('id')):
            # Set movie to movie with matchin id from movies
            movie = movie_index

    # Put page title and movie to be passed in context
    context = {
        "page_title": "Movie",
        "movie": movie,
    }

    print(context)
    # Render movies template with context
    return render(request, "movie.html", context)
