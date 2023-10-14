from django.shortcuts import render,redirect
from .models import Book, Review
from .forms import BookForm, ReviewForm

# Create your views here.
def index(request):
    books = Book.objects.all()
    context = {
        'books':books,
    }
    return render(request, 'libraries/index.html', context)


def detail(request, book_pk):
    book = Book.objects.get(pk=book_pk)
    context = {
        'book':book,
    }
    return render(request, 'libraries/detail.html', context)


def create(request):
    if request.method=='POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('libraries:index')
    else:
        form = BookForm()
    context = {
        'form':form,
    }
    return render(request, 'libraries/create.html', context)