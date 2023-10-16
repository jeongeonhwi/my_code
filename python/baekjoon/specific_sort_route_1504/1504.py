import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


from heapq import heappop,heappush
def daic(start):
    visited = [int(2e9)]*N
    visited[start[1]] = 0
    hq = [start]
    while hq:
        cnt,i,myset = heappop(hq)
        if visited[i] < cnt:
            continue
        for ni in arr[i]:
            nextcnt = cnt+ni[1]
            if visited[ni[0]] <= nextcnt:
                continue
            visited[ni[0]] = nextcnt
            heappush(hq, (nextcnt,ni[0]))
    return visited






N,E = map(int, input().split())
arr = [[] for _ in range(N)]
for _ in range(E):
    a,b,c = map(int, input().split())
    arr[a-1].append((b-1,c))
point = list(map(int, input().split()))
daic((0,0,set()))