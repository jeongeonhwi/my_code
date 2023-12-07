from django.shortcuts import render
import data

# Create your views here.
def food(request):
    food = data.food
    context = {
        'food':food,
    }
    return render(request, 'menus/food.html', context)

def drink(request):
    drink = data.drink
    context = {
        'drink':drink,
    }
    return render(request, 'menus/drink.html', context)

def receipt(request):
    message = request.GET.get('message')
    if message in data.food or message in data.drink:
        text = ' 주문받았습니다!'
    else:
        text = '은/는 주문이 불가합니다'
    context = {
        'message':message,
        'text':text,
    }
    return render(request, 'menus/receipt.html', context)