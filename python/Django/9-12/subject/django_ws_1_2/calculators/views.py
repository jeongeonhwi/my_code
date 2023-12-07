from django.shortcuts import render

# Create your views here.
def calculators(request):
    return render(request, 'calculators/calculators.html')

def result(request):
    one = request.GET.get('one')
    two = request.GET.get('two')
    plus = int(one) + int(two)
    minus = int(one) - int(two)
    x = int(one) * int(two)
    if int(two):
        y = int(one) / int(two)
    else:
        y = int(one)
    context = {
        'one':one,
        'two':two,
        'plus':plus,
        'minus':minus,
        'x':x,
        'y':y,
    }
    return render(request, 'calculators/result.html', context)