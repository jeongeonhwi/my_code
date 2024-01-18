import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

# 만약 정해진 값보다 크면 start 혹은 end를 낮추어준다.
# 만약 정해진 값보다 작으면 start 혹은 end를 늘려준다.
# 1cm = 10000000nano
try:
    while True:
        x = int(input())
        n = int(input())
        lego = [int(input()) for _ in range(n)]
        lego.sort()
        sl = set(lego)
        x *= 10000000
        for i in lego:
            if x-i in sl:
                if i == x-i:
                    if lego.count(i) >=2:
                        print('yes',i,x-i)
                        break
                else:
                    print('yes',i,x-i)
                    break
        else:
            print('danger')
except:
    pass