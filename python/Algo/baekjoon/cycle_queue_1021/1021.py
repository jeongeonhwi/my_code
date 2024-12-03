from collections import deque

N,M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ln = arr[:]
rn = arr[:]
left = deque([i for i in range(1,N+1)])
right = left.copy()
lc = 0
rc = 0
while ln:
    i = ln.pop(0)
    while True:
        if i == left[0]:
            left.popleft()
            break
        left.rotate(-1)
        lc+=1
while rn:
    i = rn.pop()
    while True:
        if i == right[0]:
            right.popleft()
            break
        right.rotate(1)
        rc+=1
print(min(rc,lc))