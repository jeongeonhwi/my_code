import sys
sys.stdin = open('input.txt')
# input = sys.stdin.readline
from heapq import heappush, heappop

def find_set(x):
    if x == parent[x]:
        return x
    parent[x] = find_set(parent[x])
    return parent[x]


def union(x,y):
    x = find_set(x)
    y = find_set(y)
    if x <= y:
        parent[y] = x
    else:
        parent[x] = y


n = int(input())
m = int(input())
cnt = 1
ans = 0
computer = [i for i in range(n+1)]
parent = [i for i in range(n+1)]
arr = []
for _ in range(m):
    a,b,c = map(int, input().split())
    heappush(arr, (c,a,b))
while arr:
    c,a,b = heappop(arr)
    if find_set(a) == find_set(b):
        continue

    union(a,b)
    ans+=c
    cnt+=1
    if cnt == n:
        break
print(ans)