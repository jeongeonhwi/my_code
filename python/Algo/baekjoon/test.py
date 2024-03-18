<<<<<<< HEAD
a = ['a','b']
b = ['a', 'c']
c = ['a','b']

if a == c:
    print('gggg')
else:
    print('bbbbb')
=======
from heapq import heappop, heappush

n,s,a,b,fares = 6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]

def solution(n, s, a, b, fares):
    arr = [[] for _ in range(n + 1)]
    ans = int(2 ** 9)
    for f in fares:
        arr[f[0]].append((f[1], f[2]))
        arr[f[1]].append((f[0], f[2]))
    def daic(start, e, c):
        dv = [int(2 ** 9) for _ in range(n + 1)]
        hq = [(c, start)]
        dv[start] = c
        while hq:
            cost, i = heappop(hq)
            if dv[i] < cost:
                continue
            for ni, nc in arr[i]:
                nextcost = nc + cost
                if dv[ni] <= nextcost:
                    continue
                dv[ni] = nextcost
                heappush(hq, (nextcost, ni))
        return dv[e]

    def dfs():
        global ans
        visited = [0 for _ in range(n + 1)]
        stack = [(0, s)]
        visited[s] = 1
        while stack:
            c, i = stack.pop()
            for ni, nc in arr[i]:
                if visited[ni] == 0:
                    visited[ni] = 1
                    stack.append((c + nc, ni))
                    aa = daic(ni, a, nc + c)
                    bb = daic(ni, b, nc + c)
                    print(aa,bb)
                    ans2 = (min(aa, bb))
                    ans = min(ans, ans2)

    dfs()

    print(ans)
    return ans
solution(n,s,a,b,fares)
>>>>>>> b548fd2c1b6fcabea28b1f758f16152e7c60bac7
