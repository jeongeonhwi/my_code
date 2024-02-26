import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

from heapq import heappop,heappush

n,l = map(int, input().split())
arr = list(map(int, input().split()))
cnt = l
save = []

for i in arr:
    heappush(save, i)
    cnt -= 1
    print(save[0], end=' ')
    if cnt == 0:
        cnt = l
        heappop(save)