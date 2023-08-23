import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    s = ''
    for _ in range(N):
        a = input().strip()
        s += a
    print(f'#{tc} ', end='')
    num = []
    for i in range(0, len(s), 7):
        num.append(s[i:i+7])
    # print(num)
    for i in range(len(num)):
        idx = num[i].find('1')
        # print(idx)
        if idx == -1:
            print(0, end=' ')
        count = 0
        if idx != -1:
            for j in range(idx, 7):
                if num[i][j] == '1':
                    count += 2**(6-j)
            print(count, end= ' ')
    print()
