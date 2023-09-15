import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

N = int(input())
arr = [[0]*100 for _ in range(100)]
for _ in range(N):
    x, y, d, g = map(int, input().split())
    cnt = 0
    arr[y][x] = 1
    ci = y
    cj = x
    q = [(ci,cj)]
    while True:
        if cnt == 0:
            if d == 0:
                arr[y][x+1] = 1
                cj += 1
            elif d == 1:
                arr[y-1][x] = 1
                ci -= 1
            elif d == 2:
                arr[y][x-1] = 1
                cj -= 1
            elif d == 3:
                arr[y+1][x] = 1
                ci += 1
        else:
            tmpq = q[:]
            tmpci, tmpcj = tmpq.pop(0)
            q.append((ci,cj))
            ci += tmpcj - cj
            cj += tmpci - ci
            while tmpq:
                i, j = tmpq.pop()
                ni = ci + (j - cj)
                nj = cj + (i - ci)
                arr[ni][nj] = 1
                q.append((ni,nj))
        print(q)
        if cnt == g:
            break
        else:
            cnt += 1
# for a in arr:
#     print(a)