from django.shortcuts import render
import random
from datetime import datetime

# Create your views here.
def hello(request):
    return render(request, 'articles/hello.html')

def ssafy(request):
    return render(request, 'articles/ssafy.html')

def get_money(request):
    # DB에서 값을 가지고 오거나 사용자의 입력을 받아서 채울 수 있음
    # 아직 배우지 않아서 직접 변수에다가 값을 넣고 진행
    name = 'ssafy'
    account = '012-34567-89012'
    money = 40000

    # context 는 html에서 사용할 값을 전달해 주는 부분
    # 반드시 데이터 타입은 딕셔너리여야 한다.
    context = {
        'name' : name,
        'account' : account,
        'money' : money,
    }
    return render(request, 'articles/bank.html', context)


# def lotto(request):
#     num = []
#     for i in range(1, 46):
#         num.append(i)
#     lotto_num = random.sample(num, 6)
#     context = {}
#     for idx, i in enumerate(lotto_num):
#         context[f'{idx+1}'] = i
#     print(context)
#     return render(request, 'articles/lotto.html', context)


def lotto(request):
    num = []
    for i in range(1, 46):
        num.append(i)
    lotto_num = random.sample(num, 6)
    context = {
        'lotto_num' : lotto_num
    }
    return render(request, 'articles/lotto.html', context)


def menus(request):
    menus = ['치킨', '돈까스', '보쌈', '피자', '햄버거']
    users = []    # [] 빈리스트로도 테스트
    today = datetime.now()

    context = {
        'menus' : menus,
        'users' : users,
        'today' : today,
    }

    return render(request, 'articles/menus.html', context)