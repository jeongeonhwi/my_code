import sys
sys.stdin = open('input.txt', 'r')



import heapq


def prim(start):
    pq = []
    heapq.heappush(pq, (0, start))
    mst = [0]*(V+1)
    sum_w = 0
    while pq:
        w, v = heapq.heappop(pq)
        if mst[v]:
            continue
        mst[v] = 1
        sum_w += w
        for weight, next in arr[v]:
            if mst[next]:
                continue
            heapq.heappush(pq, (weight, next))
    return sum_w


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = [[] for _ in range(V+1)]
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        arr[n1].append((w, n2))
        arr[n2].append((w, n1))
    ans = prim(0)
    print(f'#{tc} {ans}')