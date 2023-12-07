from django.shortcuts import render

# Create your views here.
def throw(request):
    return render(request, 'throw_loops/first/')

def first(request):
    message = request.GET.get('message')
    if not message:
        message = 'nothing'
    context = {
        'message': message,
    }
    return render(request, 'throw_loops/first.html', context)

def second(request):
    message = request.GET.get('message')
    context = {
        'message': message,
    }
    return render(request, 'throw_loops/second.html', context)

def third(request):
    message = request.GET.get('message')
    message2 = request.GET.get('message2')
    context = {
        'message': [message,message2],
    }
    return render(request, 'throw_loops/third.html', context)
