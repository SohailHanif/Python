from atexit import register
from django.shortcuts import render
# Import HTTP
from django.http import HttpResponse
# Import redirect
from django.shortcuts import redirect

from .forms import MovieForm

# Import movie model from models
from .models import Movie

# Import User Model
from django.contrib.auth.models import User
# Import authenticate, login and logout functions
from django.contrib.auth import authenticate, login, logout
# Import decorator to check login for view
from django.contrib.auth.decorators import login_required
# Import UserCreationForm
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

# View to handle user login


def loginPage(request):
    # Used in login_or_register to determine page
    page = 'login'
    # Check is user is logged in
    if request.user.is_authenticated:
        # Redirect to home if logged in
        return redirect('/')

    # Submitted login form
    if request.method == 'POST':
        # Get email and password
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        # Try to get user by username
        try:
            user = User.objects.get(username=username)
        except:
            print('User does not exist')

        # Verify password entered matches user password hash
        user = authenticate(request, username=username, password=password)

        # If user was returned
        if user is not None:
            # Login and set cookie
            login(request, user)
            return redirect('/')
        else:
            print('Invalid username or passwors')

    # Render login_register page
    context = {'page': page}
    return render(request, 'login_register.html', context)

# Function to logout user


def logoutUser(request):
    # Call user logout function to logout
    logout(request)
    return redirect('/')

# Function to register new user
def registerUser(request):
    # Get UserCreationForm from django
    form = UserCreationForm()

    if request.method == 'POST':
        # Pass form data to form
        form = UserCreationForm(request.POST)
        # If no errors in form
        if form.is_valid():
            # Build user object
            user = form.save(commit=False)
            user.username = user.username.lower()
            # Save new user in database
            user.save()
            # Login as new user
            login(request, user)
            # Redirect home
            return redirect('/')
        else:
            print("Error in registration")

    # Render register form
    return render(request, 'login_register.html', {'form': form})


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

# Use decorator to check if user is logged
# in before they can add a movie


@login_required(login_url="login")
def addMovie(request):
    # Create movie form object
    form = MovieForm()
    # When form submitted
    if request.method == 'POST':
        # Create movie object from form
        Movie.objects.create(
            posted_by=request.user,
            name=request.POST.get('name'),
            description=request.POST.get('description'),
            year=request.POST.get('year'),
            rating=request.POST.get('rating')
        )
        # Redirect to homepage
        return redirect('/')

    context = {'form': form}
    return render(request, 'movie_form.html', context)


@login_required(login_url="login")
# View to update movie with form
def updateMovie(request, pk):
    # Get movie object from db with id by using model
    movie = Movie.objects.get(id=pk)
    # Generate Movieform for movie
    form = MovieForm(instance=movie)

    # User need to be logged in as well as
    # The user that posted the movie
    if request.user != movie.posted_by:
        return render(request, "not_authorized.html")

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


@login_required(login_url="login")
def deleteMovie(request, pk):
    # Get movie object from db using model
    movie = Movie.objects.get(id=pk)

    # User need to be logged in as well as
    # The user that posted the movie
    if request.user != movie.posted_by:
        return render(request, "not_authorized.html")

    if request.method == 'POST':
        # Delete movie object and dbs
        movie.delete()
        # Returb home
        return redirect('/')
    # Render confirm delete page
    return render(request, 'delete.html', {'obj': movie})
