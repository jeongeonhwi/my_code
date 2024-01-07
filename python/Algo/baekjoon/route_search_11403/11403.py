import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

from collections import deque
def dfs(s,e):
    visited = [0]*N
    stack = deque([s])
    while stack:
        i = stack.popleft()
        for ni in range(N):
            if arr[i][ni] == 1 and visited[ni] == 0:
                visited[ni] = 1
                stack.append(ni)
                if ni == e:
                    return 1
    return 0


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            ans[i][j] = 1
        else:
            ans[i][j] = dfs(i,j)
for i in ans:
    print(*i)