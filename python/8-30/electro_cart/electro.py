import sys
sys.stdin = open('input.txt', 'r')

def suneol(i, n):
    if i == n:
        c = p[:]
        numlist.append(c)
        return
    else:
        for j in range(n):
            if used[j] == 0:
                p[i] = num[j]
                used[j] = 1
                suneol(i+1, n)
                used[j] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    num = []      # [2, 3]
    numlist = []
    for i in range(2, N+1):
        num.append(i)
    # print(num)
    n = N-1
    used = [0]*n
    p = [0]*n
    suneol(0, n)
    for i in numlist:
        i.insert(0, 1)
        i.append(1)
