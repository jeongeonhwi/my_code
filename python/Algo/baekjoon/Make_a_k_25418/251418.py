import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline
from collections import deque


def bfs(a):
    deq = deque([(a,0)])
    visited = [0]*1000001
    visited[a] = 1
    while deq:
        i,c = deq.popleft()
        for ni in [i+1, i*2]:
            if ni == K:
                return c+1
            if ni < K and visited[ni] == 0:
                visited[ni] = 1
                deq.append((ni,c+1))


A,K = map(int, input().split())

print(bfs(A))