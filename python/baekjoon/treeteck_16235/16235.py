import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# x,y 위치 인덱스2 나무 나이
tree = [list(map(int, input().split())) for _ in range(M)]
ground = [[5]*N for _ in range(N)]

tree = deque(tree)
seoson = 0
year = 0
while True:
    if year == K:
        break
    if seoson%4==0:
