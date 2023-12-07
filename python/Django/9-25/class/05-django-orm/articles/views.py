from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    # DB에서 전체 게시글을 조회 후 받은 전체 게시글 데이터를 변수에 담아
    articles = Article.objects.all()
    # index 템플릿에서 사용할 수 있도록 전달
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article':article,
    }
    return render(request, 'articles/detail.html', context)


def new(request):
    return render(request, 'articles/new.html')


def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    # 첫번째 방법
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()
    # 두번째 방법
    article = Article(title=title, content=content)
    article.save()
    # 세번째 방법
    # Article.objects.create(title=title, content=content)
    # return render(request, 'articles/create.html')
    return redirect('articles:index')


def delete(request, pk):
    # 몇번 게시글을 삭제할 것인지 조회
    article = Article.objects.get(pk=pk)
    # 조회한 게시글 삭제
    article.delete()
    return redirect('articles:index')


def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article':article,
    }
    return render(request, 'articles/edit.html', context)


def update(request, pk):
    title = request.POST.get('title')
    content = request.POST.get('content')
    # 수정하고자 하는 게시글을 조회
    article = Article.objects.get(pk=pk)
    article.title = title
    article.content = content
    article.save()
    return redirect('articles:detail', article.pk)