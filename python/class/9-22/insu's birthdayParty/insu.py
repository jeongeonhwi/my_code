import sys
sys.stdin = open('input.txt', 'r')


import heapq


def dijkstra(start, end):
    distance = [int(1e9)]*N
    pq = []
    heapq.heappush(pq, (0,start))
    distance[start] = 0
    while pq:
        dist, now = heapq.heappop(pq)
        if distance[now] < dist:
            continue
        for next in arr[now]:
            new_cost = dist+next[0]
            if distance[next[1]] <= new_cost:
                continue
            distance[next[1]] = new_cost
            heapq.heappush(pq, (new_cost, next[1]))
    return distance[end]




T = int(input())
for tc in range(1, T+1):
    N,M,X = map(int, input().split())
    arr = [[] for i in range(N)]
    number = [i for i in range(N)]
    max_v = 0
    for _ in range(M):
        x, y, c = map(int, input().split())
        arr[x-1].append((c, y-1))
    ans = 0
    for i in number:
        if i == X-1:
            continue
        go = dijkstra(i, X-1)
        come = dijkstra(X-1, i)
        ans = max(ans, go+come)
    print(f'#{tc} {ans}')