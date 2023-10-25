import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


from heapq import heappop, heappush
def daic(start):
    visited = [int(2e9)]*N
    visited[0] = 0
    hq = [start]
    while hq:
        c, i = heappop(hq)
        if visited[i] < c:
            continue
        for ni,cow in arr[i]:
            nc = c+cow
            if visited[ni] <= nc:
                continue
            visited[ni] = nc
            heappush(hq, (nc,ni))
    return visited[N-1]




# 시작점 0에서 N-1까지 가면 끝^^
N, M = map(int, input().split())
arr = [[] for _ in range(N)]
for _ in range(M):
    a,b,cnt = map(int, input().split())
    arr[a-1].append((b-1, cnt))
    arr[b-1].append((a-1, cnt))
ans = daic((0,0))
print(ans)