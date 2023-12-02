import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

def dfs(si,sj):
    stack = [(si,sj)]
    while stack:
        i,j = stack.pop()
        arr[i][j] = 0
        for di,dj in [(0,1),(1,0),(0,-1),(-1,0)]:
            ni,nj = i+di,j+dj
            if 0<=ni<M and 0<=nj<N and arr[ni][nj] == 1:
                stack.append((ni,nj))


T = int(input())
arr = [[0]*50 for _ in range(50)]
for _ in range(T):
    M, N, K = map(int, input().split())
    for _ in range(K):
        ki,kj = map(int, input().split())
        arr[ki][kj] = 1
    cnt = 0
    for i in range(M):
        for j in range(N):
            if arr[i][j] == 1:
                dfs(i,j)
                cnt += 1
    print(cnt)