import sys
input = sys.stdin.readline

n,m = map(int, input().split())
a = []
aset = set()
for _ in range(n):
    b = int(input())
    a.append(b)
    aset.add(b)
a.sort()
for _ in range(m):
    b = int(input())
    if b not in aset:
        print(-1)
        continue
    left,right = 0,n
    while left<right:
        mid = (left+right)//2
        if a[mid] < b:
            left = mid+1
        else:
            right = mid
    print(left)