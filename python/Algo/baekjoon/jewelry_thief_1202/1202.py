import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline
from heapq import heappush, heappop


N,K = map(int, input().split())
jewelry = []
bag = []
for _ in range(N):
    data = list(map(int, input().split()))
    heappush(jewelry, data)
for _ in range(K):
    heappush(bag, int(input()))
available_jewelry = []
max_v = 0
while bag:
    b = heappop(bag)
    while jewelry and jewelry[0][0] <= b:
        w,v = heappop(jewelry)
        heappush(available_jewelry, -v)
    if available_jewelry:
        v = heappop(available_jewelry)
        max_v -= v
print(max_v)