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
        if n==0 or n==1:
            print('danger')
        elif n == 2:
            if lego[0] + lego[1] == x*10000000:
                print(f'yes {lego[0]} {lego[1]}')
            else:
                print('danger')
        else:
            x *= 10000000
            mid = x/2
            one = []
            two = []
            m = []
            for i in range(n):
                if lego[i] < mid:
                    one.append(lego[i])
                elif lego[i] > mid:
                    two.append(lego[i])
                else:
                    m.append(lego[i])
            print(one,two,m)
            two2 = set(two)
            for i in one:
                if x-i in two2:
                    print(f'yes {i} {x-i}')
                    break
            else:
                if len(m) >= 2:
                    print(f'yes {m[0]} {m[0]}')
                else:
                    print('danger')
except:
    pass