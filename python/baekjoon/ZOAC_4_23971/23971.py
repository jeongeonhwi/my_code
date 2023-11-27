import sys
sys.stdin = open('input.txt', 'r')

H, W, N, M = map(int, input().split())
max_v = 0
width = 0
heigh = 0
width, heigh = H//(N+1), W//(M+1)
if H%(N+1) > 0:
    width += 1
if W%(M+1) > 0:
    heigh += 1
print(width*heigh)