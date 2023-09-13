from django.shortcuts import render
import random
import data

# Create your views here.
def certi1(request):
    context = {
        'name':'Kim happy',
        'age':random.choice(data.age),
        'grade':random.choice(data.grade),
    }
    return render(request, 'certifitations/certifitations1.html', context)

def certi2(request):
    context = {
        'name':'park happy',
        'age':random.choice(data.age),
        'grade':random.choice(data.grade),
    }
    return render(request, 'certifitations/certifitations2.html', context)

def certi3(request):
    context = {
        'name':'lee happy',
        'age':random.choice(data.age),
        'grade':random.choice(data.grade),
    }
    return render(request, 'certifitations/certifitations3.html', context)