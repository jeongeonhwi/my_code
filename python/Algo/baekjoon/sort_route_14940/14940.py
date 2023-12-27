import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

from heapq import heappop, heappush
def findgoal():
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 2:
                return (i,j)

def dfs(gi,gj):
    visited = [[float('inf')]*M for _ in range(N)]
    hq = [(0,gi,gj)]
    visited[gi][gj] = 0
    while hq:
        cnt, i,j = heappop(hq)
        if visited[i][j] >= cnt:
            for di,dj in [(-1,0),(1,0),(0,-1),(0,1)]:
                ni,nj = di+i,dj+j
                if 0<=ni<N and 0<=nj<M and arr[ni][nj] != 0:
                    if visited[ni][nj] > cnt+1:
                        visited[ni][nj] = cnt+1
                        heappush(hq, (cnt+1,ni,nj))
    return visited


N,M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
gi,gj = findgoal()
ans = dfs(gi,gj)
for i in range(N):
    for j in range(M):
        if ans[i][j] == float('inf'):
            if arr[i][j] == 1:
                print(-1, end=' ')
            else:
                print(0, end=' ')
        else:
            print(ans[i][j], end=' ')
    print()