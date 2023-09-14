from django.shortcuts import render

# Create your views here.
def first(request):
    order = request.GET.get('order')
    if order:
        order = f'{order} 을/를 받음!'
    else:
        order = '아무것도 받지 못함'
    context = {
        'order':order
    }
    return render(request, 'throw_catch/first.html', context)

def second(request):
    order = request.GET.get('order')
    if order:
        order = f'{order} 을/를 받음!'
    else:
        order = '아무것도 받지 못함'
    context = {
        'order':order
    }
    return render(request, 'throw_catch/second.html', context)