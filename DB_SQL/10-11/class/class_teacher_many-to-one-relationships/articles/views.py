from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Article, Comment
from .forms import ArticleForm, CommentForm


# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    form = CommentForm()
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/detail.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


@login_required
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


@login_required
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid:
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)


def comment_create(request, comment_pk):
    form = CommentForm(request.POST)
    article = Article.objects.get(pk=comment_pk)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.article = article
        comment.save()
        return redirect('articles:detail', article.pk)
    context = {
        # article 정보도 전달해야함
        # article의 디테일 페이지 이기 때문
        'form':form,
        'article': article,
    }
    # redirect는 새롭게 요청을 하는 것이기 때문에 에러 정보를 전달할 수 없다.
    # render를 하는 이유는 
    # 에러 정보를 전달하기 위해서!!!
    return render(request, 'articles/detail.html', context)


def comment_delete(request, article_pk,comment_pk):
    # 댓글을 삭제해야 하는데 ... 어떤 댓글을 삭제하죠?
    # => 삭제하려는 댓글 정보가 필요하다!!
    # => 삭제하려는 댓글의 pk 정보를 variable routing 으로 가져오자
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)