from django.shortcuts import render,redirect
from .forms import MovieForm, CommentForm
from .models import Movie, Comment

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies':movies,
    }
    return render(request, 'movies/index.html', context)


def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.user_id = request.user
            form.save()
            return redirect('movies:index')
    else:
        form = MovieForm()
    context = {
        'form':form,
    }
    return render(request, 'movies/create.html', context)


def detail(request, user_pk):
    movie = Movie.objects.get(pk=user_pk)
    context = {
        'movie':movie,
    }
    return render(request, 'movies/detail.html', context)