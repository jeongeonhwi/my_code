import sys
sys.stdin = open('input.txt', 'r')

from collections import deque


def find_one(arr):
    visited = [[0]*M for _ in range(N)]
    q = []
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                q.append((i,j))
                visited[i][j] = 1
            elif arr[i][j] == -1:
                visited[i][j] = 1
    return q, visited


def bfs(arr):
    q, visited = find_one(arr)
    q = deque(q)
    while q:
        i, j = q.popleft()
        for k in range(4):
            ni = i+di[k]
            nj = j+dj[k]
            if 0<=ni<N and 0<=nj<M and visited[ni][nj] == 0 and arr[ni][nj]==0:
                q.append((ni,nj))
                visited[ni][nj] = visited[i][j]+1
    min_v = max(map(max, visited))
    cnt = 0
    for i in visited:
        cnt += i.count(0)
    if cnt > 0:
        min_v = -1
    return min_v

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]
M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
min_v = bfs(arr)-1
if min_v == -2:
    min_v = -1
print(min_v)