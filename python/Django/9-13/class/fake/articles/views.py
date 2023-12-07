from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')

def detail(request, user_id, article_pk):
    context = {
        'user_id' : user_id,
        'article_pk' : article_pk,
    }
    return render(request, 'articles/detail.html', context)