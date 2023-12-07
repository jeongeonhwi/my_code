import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline



from copy import deepcopy
from itertools import combinations
def find_virus():
    virus = set()
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 2:
                virus.add((i,j))
    return virus


def dfs(v):
    stack = [v]
    while stack:
        vi,vj = stack.pop()
        for k in range(4):
            ni,nj = vi+di[k],vj+dj[k]
            if 0<=ni<N and 0<=nj<M and arr2[ni][nj] != 1 and arr2[ni][nj] != 2:
                arr2[ni][nj] = 1
                stack.append((ni,nj))




di = [1,0,-1,0]
dj = [0,-1,0,1]
# 0은 빈칸 1은 벽 2는 바이러스 위치
N,M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
virus = find_virus()
position = []
max_v = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            position.append((i,j))
combi = combinations(position,3)
for com in combi:
    arr2 = deepcopy(arr)
    for ci,cj in com:
        arr2[ci][cj] = 1
    for v in virus:
        dfs(v)
    zero = 0
    for z in arr2:
        zero += z.count(0)
    max_v = max(max_v, zero)
print(max_v)