from django.shortcuts import render
import data

# Create your views here.
def prices(request, thing, cnt):
    if thing in data.product_price:
        total = data.product_price.get(thing)*cnt
        order = f'{thing} {cnt}개의 가격은 {total}원 입니다.'
    else:
        order = thing+'은/는 없어용'

    context = {
        'order': order
    }
    return render(request, 'prices/price.html', context)