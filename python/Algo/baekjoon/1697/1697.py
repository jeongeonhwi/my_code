import sys
sys.stdin = open('input.txt', 'r')

from collections import deque


N, K = map(int, input().split())
check = True
if N == K:
    print(0)
    check = False
elif N>K:
    print(N-K)
    check = False
if check:
    min_v = float('inf')
    q = deque()
    visited = [0]*100001
    q.append(N)
    while q:
        i = q.popleft()
        if i == K:
            print(visited[i])
            break
        for k in (1, -1, i):
            if 0<=i+k<100001 and visited[i+k] == 0:
                q.append(i+k)
                visited[i+k] = visited[i]+1
