import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

def dfs(si,sj):
    stack = [(si,sj)]
    visited[si][sj] = 1
    cnt = 1
    while stack:
        i,j = stack.pop()
        for ni,nj in [(i+1,j),(i,j+1),(i-1,j),(i,j-1),]:
            if 0<=ni<n and 0<=nj<m and visited[ni][nj] == 0 and arr[ni][nj] == 1:
                stack.append((ni,nj))
                visited[ni][nj] = 1
                cnt += 1
    return cnt


n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
paint_cnt = 0
pm = 0
for i in range(n):
    for j in range(m):
        if visited[i][j] == 0 and arr[i][j] == 1:
            paint_cnt += 1
            pm = max(pm, dfs(i,j))
print(paint_cnt)
print(pm)