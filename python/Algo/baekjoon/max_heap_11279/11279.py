import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

from heapq import heappush,heappop
N = int(input())
hq = []
for _ in range(N):
    data = int(input())
    if data != 0:
        heappush(hq, -data)
    else:
        if hq:
            print(-heappop(hq))
        else:
            print(0)