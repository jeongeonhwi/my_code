import sys
input = sys.stdin.readline



def f(p, c):
    global min_v
    print(min_v)
    if min_v <= c:
        return
    for i in range(ncnt):
        bcheck = False
        if N[i] == 'b':
            for j in range(bcnt):
                if N[(i+j)%ncnt] != 'b':
                    bcheck = True
                    break
            else:
                min_v = min(min_v, c)
                return
        if bcheck:
            break
    if p < ncnt:
        for i in range(p+1, ncnt):
            N[p], N[i] = N[i], N[p]
            f(p+1, c+1)
            N[p], N[i] = N[i], N[p]



N = list(input())
N.pop()
ncnt = len(N)
acnt = N.count('a')
bcnt = N.count('b')
min_v = float('inf')
f(0, 0)

print(min_v)