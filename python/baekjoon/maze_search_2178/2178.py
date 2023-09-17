import sys


from collections import deque
def bfs(arr):
    visited = [[0]*M for _ in range(N)]
    q = [(0,0)]
    q = deque(q)
    visited[0][0] = 1
    while q:
        i, j = q.popleft()
        if i == N-1 and j == M-1:
            return visited[i][j]
        for k in range(4):
            ni = i+di[k]
            nj = j+dj[k]
            if 0<=ni<N and 0<=nj<M and visited[ni][nj] == 0 and arr[ni][nj] == '1':
                visited[ni][nj] = visited[i][j]+1
                q.append((ni,nj))


di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]
N, M = map(int, input().split())
arr = [sys.stdin.readline() for _ in range(N)]
ans = bfs(arr)
print(ans)