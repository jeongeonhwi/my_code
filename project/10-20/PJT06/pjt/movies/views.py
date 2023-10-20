from django.shortcuts import render, redirect, get_list_or_404,get_object_or_404
from .models import Movie, Comment
from .forms import CommentForm, MovieForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    movies = get_list_or_404(Movie)
    context = {
        'movies':movies,
    }
    return render(request, 'movies/index.html', context)


def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    comment_form = CommentForm()
    comments = movie.comment_set.all()
    context = {
        'movie':movie,
        'comment_form':comment_form,
        'comments':comments
    }
    return render(request, 'movies/detail.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.user = request.user
            form.save()
            return redirect('movies:detail', movie.pk)
    elif request.method == 'GET':
        form = MovieForm
    context = {
        'form':form,
    }
    return render(request, 'movies/create.html', context)


@login_required
def delete(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.user == movie.user:
        movie.delete()
    return redirect('movies:index')


@login_required
def update(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.user == movie.user:
        if request.method == 'POST':
            form = MovieForm(request.POST, instance=movie)
            if form.is_valid():
                form.save()
                return redirect('movies:detail', movie.pk)
        else:
            form = MovieForm(instance=movie)
    else:
        return redirect('movies:index')
    context = {
        'movie': movie,
        'form':form,
    }
    return render(request, 'movies/update.html', context)


@login_required
def comment_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.movie = movie
        comment.user = request.user
        comment_form.save()
        return redirect('movies:detail', movie.pk)
    context = {
        'movie':movie,
        'comment_form':comment_form,
    }
    return render(request, 'movies/detail.html', context)


@login_required
def comment_delete(request, movie_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('movies:detail', movie_pk)


@login_required
def likes(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.user in movie.like_users.all():
        movie.like_users.remove(request.user)
    else:
        movie.like_users.add(request.user)
    return redirect('movies:index')