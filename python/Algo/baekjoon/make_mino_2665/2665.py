import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

from heapq import heappop, heappush

def daic(arr):
    n,m = len(arr), len(arr[0])
    visited = [[float('inf')]*m for _ in range(n)]
    visited[0][0] = 0
    hq = [(0,0,0)]
    while hq:
        c,i,j = heappop(hq)
        if visited[i][j] < c:
            continue
        for di,dj in [(0,1),(1,0),(0,-1),(-1,0)]:
            ni,nj = i+di, j+dj
            if 0<=ni<n and 0<=nj<m:
                nc = c
                if arr[ni][nj] == '0':
                    nc += 1
                if visited[ni][nj] <= nc:
                    continue
                visited[ni][nj] = nc
                heappush(hq, (nc,ni,nj))
    return visited[n-1][m-1]


N = int(input())
arr = [input().strip() for _ in range(N)]
print(daic(arr))