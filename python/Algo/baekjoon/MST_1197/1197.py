import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline
from heapq import heappush, heappop

def daic(source_node):
    visited = [0]*(V+1)
    hq = [(0,source_node)]
    w_cnt = 0
    while hq:
        w,node = heappop(hq)
        if visited[node] ==1:
            continue
        visited[node] = 1
        w_cnt += w
        for next_node, nw in arr[node]:
            if visited[next_node] == 1:
                continue
            heappush(hq, (nw, next_node))
    return w_cnt

V,E = map(int, input().split())
arr = [[] for _ in range(V+1)]
for _ in range(E):
    node, linked_node, weight = map(int, input().split())
    arr[node].append((linked_node, weight))
    arr[linked_node].append((node, weight))

print(daic(1))