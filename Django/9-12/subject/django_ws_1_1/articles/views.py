from django.shortcuts import render
import data

# Create your views here.
def fruit(request):
    context = {
        'fruit_list': data.fruit_list,
        'hate': data.hate,
    }
    return render(request, 'articles/fruit.html', context)