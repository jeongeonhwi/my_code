from django.shortcuts import render

# Create your views here.
def calculators(request, one, two):
    plus = one+two
    plus = f'{one} + {two} = {plus}'
    x = one*two
    x = f'{one} * {two} = {x}'
    minus = one-two
    minus = f'{one} - {two} = {minus}'
    if two:
        y = one/two
        y = f'{one} / {two} = {y}'
    else:
        y = '계산할 수 없습니다.'
    context = {
        'plus':plus,
        'x':x,
        'minus':minus,
        'y':y,
    }
    return render(request, 'calculators/calculators.html', context)