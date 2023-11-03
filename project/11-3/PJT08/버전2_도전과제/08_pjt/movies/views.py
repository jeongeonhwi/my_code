from django.shortcuts import render, redirect
from django.views.decorators.http import require_safe
from django.contrib.auth.decorators import login_required
from .models import Movie
from community.forms import CommentForm
from .forms import MovieForm
from community.models import Comment


# Create your views here.
@require_safe
def index(request):
    movies = Movie.objects.order_by('-pk')
    # recommended_movies = []
    # for m in range(3):
    #     recommended_movies.append(movies[m])
    
    context = {
        'movies': movies,
        # 'recommended_movies': recommended_movies,
    }
    return render(request, 'movies/index.html/', context)


@require_safe
def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    # comment_form = CommentForm()
    # comments = movie.comment_set.all()
    context = {
        'movie': movie,
        # 'comment_form': comment_form,
        # 'comments': comments,
    }
    return render(request, 'movies/detail.html', context)


@require_safe
def recommended(request):
    movies = Movie.objects.order_by('-popularity')
    recommended_movies = []
    most_recommended = []
    for m in range(10):
        recommended_movies.append(movies[m])
        if m < 3:
            most_recommended.append(movies[m])
    
    
    context = {
        'movies': movies,
        'recommended_movies': recommended_movies,
        'most_recommended': most_recommended,
    }
    return render(request, 'movies/recommended.html/', context)


