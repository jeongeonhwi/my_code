import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline
sys.setrecursionlimit(10*6)

def dfs(i,j):
    if visited[i][j]:
        return visited[i][j]

    visited[i][j] = 1

    for ni,nj in [(i+1,j),(i,j+1),(i-1,j),(i,j-1),]:
        if 0<=ni<N and 0<=nj<N and arr[i][j] < arr[ni][nj]:
            visited[i][j] = max(visited[i][j], dfs(ni,nj)+1)
    return visited[i][j]



N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
max_v = 0
for i in range(N):
    for j in range(N):
        max_v = max(max_v, dfs(i,j))

print(max_v)