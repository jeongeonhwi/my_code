import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')


def f(p, c):
    global min_v
    if N.count('a') == ncnt:
        min_v = 0
        return
    if min_v <= c:
        return
    for i in range(ncnt):
        bcheck = False
        if N[i] == 'b':
            for j in range(bcnt):
                if N[(i+j)%ncnt] != 'b':
                    break
            else:
                min_v = min(min_v, c)
                print(N, c, min_v)
                return
    for i in range(ncnt):
        if p == i:
            continue
        if p >= ncnt:
            return
        if N[p] == 'a':
            continue
        if visited[i]:
            continue
        N[p],N[i] = N[i],N[p]
        visited[i] = 1
        for j in range(ncnt):
            if visited[j]:
                continue
            if N[j] == 'b':
                continue
            visited[j] = 1
            f(j,c+1)
            visited[j] = 0
        visited[i] = 0
        N[p], N[i] = N[i], N[p]


# a = 0, b = 1
N = list(input())
nset = {(tuple(N),0)}
ncnt = len(N)
acnt = N.count('a')
bcnt = N.count('b')
min_v = min(acnt,bcnt) + 1
visited = [0]*ncnt
for i in range(ncnt):
    if N[i] == 'b':
        continue
    visited[i] = 1
    f(i, 0)
    visited[i] = 0
print(min_v)