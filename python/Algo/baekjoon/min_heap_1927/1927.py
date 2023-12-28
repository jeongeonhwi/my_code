import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

from heapq import heappop, heappush
N = int(input())
arr = []
for _ in range(N):
    data = int(input())
    if data == 0:
        if arr:
            print(heappop(arr))
        else:
            print(0)
    else:
        heappush(arr, data)