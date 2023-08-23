import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = float(input())
    a = N
    b_list = []
    num = 1
    overcheck = True
    while True:
        if len(b_list) > 12:
            overcheck = False
            break
        if a == (1/2)**num:
            b_list.append('1')
            break
        elif a > (1/2)**num:
            b_list.append('1')
            a -= (1/2)**num
            num += 1
        else:
            b_list.append('0')
            num += 1
    s = ''.join(b_list)
    if overcheck:
        print(f'#{tc}', end=' ')
        print(s)
    else:
        print(f'#{tc} overflow')