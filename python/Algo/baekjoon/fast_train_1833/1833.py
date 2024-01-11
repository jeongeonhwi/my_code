import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

# 음수는 이미 설치된 고석철도
# 10000을 넘지 않는 지연수는 설치 비용


from heapq import heappop, heappush

def daic(s):
    visited = [float('inf')]*(N+1)
    hq = [s]
    visited[s] = 0



N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
cost = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] < 0:
            cost += arr[i][j]
            arr[i][j] = 0
cost //= 2