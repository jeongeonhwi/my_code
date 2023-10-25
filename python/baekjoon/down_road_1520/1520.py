import sys
sys.stdin = open('input.txt', 'r')



from collections import deque
N,M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*M for _ in range(N)]
dp[0][0] = 1
visited = {(0,0)}
si, sj = 0,0
ei, ej = N-1, M-1
my = [(0,0)]
my = deque(my)
while my:
    i,j = my.popleft()
    for di,dj in [(1,0),(0,1),(-1,0),(0,-1)]:
        ni,nj = i+di,j+dj
        if 0<=ni<N and 0<=nj<M and arr[ni][nj]<arr[i][j]:
            dp[ni][nj] += dp[i][j]
            my.append((ni,nj))
for i in dp:
    print(i)
print(dp[N-1][M-1])