import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

from collections import deque
# def bfs():



N = int(input())
arr = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
visited = [0]*(N+1)
