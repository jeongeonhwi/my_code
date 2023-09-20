import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

def bfs(start):
    visited = [0]*101
    visited[start] = 1
    q = [start]
    q = deque(q)
    while q:
        i = q.popleft()
        for j in arr[i]:
            if visited[j] == 0:
                q.append(j)
                visited[j] = 1+visited[i]
    return visited




T = 10
for tc in range(1, T+1):
    length, start = map(int, input().split())
    input_data = list(map(int, input().split()))
    arr = [[] for _ in range(101)]
    for i in range(length//2):
        arr[input_data[i*2]].append(input_data[i*2+1])
    visited = bfs(start)
    max_v = max(visited)
    ans = 0
    for v in range(len(visited)-1, -1, -1):
        if max_v == visited[v]:
            ans = v
            break
    print(f'#{tc} {ans}')