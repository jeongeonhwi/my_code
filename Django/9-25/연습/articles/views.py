from django.shortcuts import render

# Create your views here.
def lunch(request, menu):
    lunch_list = {'국밥', '떡볶이', '피자', '탕수육', '삼겹살', '갈비', '짜장면'}
    # menu가 있으면 ㅇㅇ은 준비가 되었습니다. 를 html에서 출력
    if menu in lunch_list:
        res = f'{menu} 은 준비되었습니다.'
    # menu가 없으면 ㅇㅇ은 준비되지 않았습니다. 를 html에서 출력
    else:
        res = f'{menu} 은 준비되지 않았습니다.'
    context = {
        'res':res,
    }
    return render(request, 'articles/lunch.html', context)


def p1(request, hi, key):
    # h를 key로 exclusive or 를 한 결과를 출력
    # 둘다 str 형태 이기에 int로 형변환을
    # 형변환된 두 값을 ^ 한다.
    # 다시 str 으로 형변환 후 대문자로 출력
    int_key = int(key, base=16)
    res = ''
    for h in hi:
        int_h = int(h, base=16)
        calc = hex(int_h^int_key)
        res += calc[-1].upper()
    context = {
        'res':res,
    }
    return render(request, 'articles/p1.html', context)


def throw(request):
    return render(request, 'articles/throw.html')


def catch(request):
    hi = request.GET.get('hi')
    key = request.GET.get('key')
    
    return render(request, 'articles/catch.html')