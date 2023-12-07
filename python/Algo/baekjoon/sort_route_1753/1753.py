import sys
input = sys.stdin.readline

from heapq import heappop, heappush
def dijkstra(start):
    visited[start[1]] = 0
    hp = []
    heappush(hp, start)
    while hp:
        cnt, i = heappop(hp)
        if cnt > visited[i]:
            continue
        for vj,wj in arr[i]:
            next_cnt = cnt+wj
            if visited[vj] <= next_cnt:
                continue
            visited[vj] = next_cnt
            heappush(hp, (next_cnt,vj))
    return visited

V,E = map(int, input().split())
K = int(input())
arr = [[] for _ in range(V)]
visited = [float('inf')]*V
for _ in range(E):
    u,v,w = map(int, input().split())
    arr[u-1].append((v-1,w))
ans = dijkstra((0,K-1))
for i in ans:
    if type(i) == float:
        print('INF')
    else:
        print(i)