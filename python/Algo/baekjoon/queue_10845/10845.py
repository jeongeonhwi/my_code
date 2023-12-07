import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

from collections import deque
N = int(input())
q = deque()
for _ in range(N):
    data = input().strip()
    if data[:2] == 'pu':
        order, num = data.split()
        q.append(num)
        continue
    if data == 'pop':
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
        continue
    if data == 'size':
        print(len(q))
        continue
    if data == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
        continue
    if data == 'front':
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
        continue
    if data == 'back':
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])