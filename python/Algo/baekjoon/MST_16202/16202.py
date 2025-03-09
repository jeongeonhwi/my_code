import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline
from heapq import heappush, heappop

def union_set(x,y):
    x = find_set(x)
    y = find_set(y)
    if x == y:
        return
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


def find_set(x):
    if parent[x] == x:
        return x
    parent[x] = find_set(parent[x])
    return parent[x]



N,M,K = map(int, input().split())
arr = []
for m in range(1, M+1):
    x,y = map(int, input().split())
    heappush(arr, (m,x,y))

flag = False
for _ in range(K):
    parent = [i for i in range(N + 1)]
    if flag:
        print(0, end=" ")
        continue
    ans = 0
    c = 0
    used = []
    unused = []
    for _ in range(N-1):
        cc = False
        while arr:
            nm,nx,ny = heappop(arr)
            if find_set(nx) != find_set(ny):
                used.append((nm,nx,ny))
                union_set(nx,ny)
                c+=nm
                break
            else:
                unused.append((nm,nx,ny))
                if len(arr) == 0:
                    cc = True
        if cc:
            break
    else:
        ans = c
    ec = 0
    for i in range(1,N+1):
        find_set(i)
        if i == 1:
            ec = parent[i]
        else:
            if parent[i] != ec:
                ans = 0

    if ans == 0:
        print(0, end=" ")
        flag = True
    else:
        print(ans, end=" ")
        used.pop(0)
        while used:
            heappush(arr, heappop(used))
        while unused:
            heappush(arr, heappop(unused))