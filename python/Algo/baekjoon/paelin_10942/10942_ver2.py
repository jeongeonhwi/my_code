import sys
sys.stdin=open('input.txt', 'r')
# input = sys.stdin.readline


N = int(input())
arr = list(map(int, input().split()))
M = int(input())
q = [list(map(int, input().split())) for _ in range(M)]
dp = [[0]*N for _ in range(N)]

for i in range(N):
    dp[i][i] = 1

for i in range(N-1):
    if arr[i] == arr[i+1]:
        dp[i][i+1] = 1

for m in range(N-2):
    for i in range(N-2-m):
        j = i+2+m
        if arr[i] == arr[j] and dp[i+1][j-1] == 1:
            dp[i][j] = 1
# print(dp)
for _ in q:
    i,j = _
    print(dp[i-1][j-1])
