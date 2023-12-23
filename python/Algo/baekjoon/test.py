import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

from heapq import heappop, heappush
N = int(input())
stack = []
for _ in range(N):
    data = int(input())
    if data != 0:
        heappush(stack, (abs(data), data))
    else:
        if stack:
            ans = heappop(stack)
            print(ans[1])
        else:
            print(0)