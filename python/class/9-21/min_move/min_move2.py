import sys
sys.stdin = open('input.txt', 'r')


from collections import deque
def bfs(start):
    visited = [int(1e9)]*(N+1)
    q = [(0, start)]
    q = deque(q)
    visited[start] = 1
    while q:
        distance, now = q.popleft()
        for dist, next in arr[now]:
            new_dist = distance+dist
            if new_dist < visited[next]:
                visited[next] = new_dist
                q.append((new_dist, next))
    return visited[N]

T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    arr = [[] for _ in range(N+1)]
    for _ in range(E):
        start, end, di = map(int, input().split())
        arr[start].append((di, end))
    ans = bfs(0)
    print(f'#{tc} {ans}')