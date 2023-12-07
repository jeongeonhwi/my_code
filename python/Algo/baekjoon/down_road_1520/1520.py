import sys
sys.stdin = open('input.txt', 'r')



def dp(i,j):
    if i == N-1 and j == M-1:
        return 1
    if visited[i][j] != -1:
        return visited[i][j]
    visited[i][j] = 0
    for di,dj in [(1,0),(0,1),(-1,0),(0,-1)]:
        ni,nj = i+di,j+dj
        if 0<=ni<N and 0<=nj<M:
            if arr[i][j] > arr[ni][nj]:
                visited[i][j] += dp(ni,nj)
    return visited[i][j]




N,M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[-1]*M for _ in range(N)]
ans = dp(0,0)
print(ans)