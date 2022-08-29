from django.shortcuts import render
# Import HTTP
from django.http import HttpResponse
# Import redirect
from django.shortcuts import redirect

from .forms import MovieForm

# Import movie model from models
from .models import Movie 

# Create your views here.

# View for movies
def movies(request):
    # Get movies from database using Queryset
    movies = Movie.objects.all()

    # Put page title and movies array to be passed in context
    context = {
        "page_title": "Movies",
        "movies": movies,
    }

    # Render movies template with context
    return render(request, "homepage.html", context)

# View for movie based on id get param
def movie(request, pk):
    # Use movie manager(objects) to get movie where id=pk
    movie = Movie.objects.get(id=pk)
    # Put page title and movie to be passed in context
    context = {
        "page_title": "Movie",
        "movie": movie,
    }

    # Render movies template with context
    return render(request, "movie.html", context)

def addMovie(request):
    # Create movie form object
    form = MovieForm()
    # When form submitted
    if request.method == 'POST':
        # Create movie object from form
        Movie.objects.create(
            name=request.POST.get('name'),
            description=request.POST.get('description'),
            year=request.POST.get('year'),
            rating=request.POST.get('rating'),
        )
        # Redirect to homepage
        return redirect('/')

    context = {'form': form}
    return render(request, 'movie_form.html', context)

# View to update movie with form
def updateMovie(request, pk):
    # Get movie object from db with id by using model
    movie = Movie.objects.get(id=pk)
    # Generate Movieform for movie
    form = MovieForm(instance=movie)

    # When form submitted get values
    if request.method == 'POST':
        # Update model based on form values
        movie.name = request.POST.get('name')
        movie.description = request.POST.get('description')
        movie.year = request.POST.get('year')
        movie.rating = request.POST.get('rating')
        # Save model in db
        movie.save()
        # Redirect to hom
        return redirect('/')

    # Return and render movie form
    context = {'form': form, 'movie': movie}
    return render(request, 'movie_form.html', context)


# Route to delete movie
def deleteMovie(request, pk):
    # Get movie object from db using model
    movie = Movie.objects.get(id=pk)
    if request.method == 'POST':
        # Delete movie object and dbs
        movie.delete()
        # Returb home
        return redirect('/')
    # Render confirm delete page
    return render(request, 'delete.html', {'obj': movie})

