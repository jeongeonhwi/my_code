import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

from heapq import heappop, heappush
def go(start):
    visited = [int(2e9)]*N
    visited[start[1]] = 0
    hq = []
    heappush(hq, start)
    while hq:
        cnt, i = heappop(hq)
        if i == X-1:
            return cnt
        if visited[i] < cnt:
            continue
        for tj, ej in arr[i]:
            next_cnt = cnt+tj
            if visited[ej] <= next_cnt:
                continue
            visited[ej] = next_cnt
            heappush(hq, (next_cnt,ej))


def come(start,end):
    visited = [int(2e9)]*N
    visited[start[1]] = 0
    hq = []
    heappush(hq, start)
    while hq:
        cnt, i = heappop(hq)
        if i == end:
            return cnt
        if visited[i] < cnt:
            continue
        for tj, ej in arr[i]:
            next_cnt = cnt+tj
            if visited[ej] <= next_cnt:
                continue
            visited[ej] = next_cnt
            heappush(hq, (next_cnt,ej))

N,M,X = map(int, input().split())
arr = [[] for _ in range(N)]
for _ in range(M):
    s,e,t = map(int, input().split())
    arr[s-1].append((t,e-1))
max_v = 0
for i in range(N):
    tmpgo = go((0,i))
    tmpcome = come((0,X-1),i)
    max_v = max(max_v, tmpgo+tmpcome)
print(max_v)