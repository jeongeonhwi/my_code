import sys
sys.stdin = open('input.txt', 'r')

import heapq

def dijkstra(one, two):
    distance = [[int(1e9)]*N for _ in range(N)]
    pq = []
    heapq.heappush(pq, (0, one, two, arr[0][0]))
    distance[0][0] = 0
    while pq:
        f, i, j, h = heapq.heappop(pq)
        if distance[i][j] < f:
            continue
        if distance[N-1][N-1] <= f:
            continue
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N:
                if h < arr[ni][nj]:
                    if distance[ni][nj] <= f + abs(h-arr[ni][nj])+1:
                        continue
                    distance[ni][nj] = f + abs(h-arr[ni][nj])+1
                    heapq.heappush(pq, (distance[ni][nj], ni, nj, arr[ni][nj]))
                else:
                    if distance[ni][nj] <= f+1:
                        continue
                    distance[ni][nj] = f+1
                    heapq.heappush(pq, (distance[ni][nj], ni, nj, arr[ni][nj]))
    return distance[N-1][N-1]



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = dijkstra(0, 0)
    print(f'#{tc} {ans}')