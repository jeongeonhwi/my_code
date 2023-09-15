from django.shortcuts import render
from .models import Article

# Create your views here.
def index(request):
    # DB에서 전체 게시글을 조회
    articles = Article.objects.all()
    # 받은 전체 게시글 데이터를 변수에 담아서
    context = {
        'articles':articles,
    }
    # 인덱스 템플릿에서 사용할 수 있도록 전달.
    return render(request, 'index.html', context)