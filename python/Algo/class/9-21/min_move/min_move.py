import sys
sys.stdin = open('input.txt', 'r')


import heapq

def dijkstra(start):
    distance = [int(1e9)]*(N+1)
    pq = []
    heapq.heappush(pq, (0, start))
    distance[start] = 0
    while pq:
        dist, now = heapq.heappop(pq)
        if distance[now] < dist:
            continue
        for next in arr[now]:
            next_node = next[1]
            cost = next[0]
            new_cost = dist + cost
            if distance[next_node] <= new_cost:
                continue
            distance[next_node] = new_cost
            heapq.heappush(pq, (new_cost, next_node))
    return distance[N]

T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    arr = [[] for _ in range(N+1)]
    for _ in range(E):
        start, end, di = map(int, input().split())
        arr[start].append((di, end))
    ans = dijkstra(0)
    print(f'#{tc} {ans}')