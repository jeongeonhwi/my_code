import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

def bfs(start, arr):
    visited = [0]*(N+1)
    q = [start]
    q = deque(q)
    visited[start] = 1
    while q:
        i = q.popleft()
        for j in range(N+1):
            if arr[i][j] == 1 and visited[j] == 0:
                visited[j] = visited[i]+1
                q.append(j)
    return sum(visited)


N, M = map(int, input().split())
arr = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    one, two = map(int, input().split())
    arr[one][two] = 1
    arr[two][one] = 1
min_v = 100000
min_body = 1
for num in range(1, N+1):
    tmp = bfs(num, arr)
    if min_v > tmp:
        min_v = tmp
        min_body = num
    elif min_v == tmp:
        if num < min_body:
            min_body = num
print(min_body)