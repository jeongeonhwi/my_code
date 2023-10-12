import sys
sys.stdin = open('input.txt', 'r')

N, M, H = map(int, input().split())
arr = [[0]*(N+N-1)]
for _ in range(M):
