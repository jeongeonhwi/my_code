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
                return
    for i in range(ncnt):
        if p == i:
            continue
        if N[p] == N[i]:
            continue
        if p >= ncnt:
            return
        N[p],N[i] = N[i],N[p]
        if tuple(N) in nset:
            N[p], N[i] = N[i], N[p]
            continue
        nset.add(tuple(N))
        f(p+1,c+1)
        N[p], N[i] = N[i], N[p]



N = list(input())
nset = {tuple(N)}
ncnt = len(N)
acnt = N.count('a')
bcnt = N.count('b')
min_v = float('inf')
f(0, 0)
print(min_v)