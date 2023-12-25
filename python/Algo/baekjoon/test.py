import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
# print = sys.stdin.write

N,M = map(int, input().split())
arr = []
for _ in range(N):
    data = list(map(int, input().split()))
    arr.append(data)
dp = [[0]*M for _ in range(N)]
dp[0][0] = arr[0][0]
for j in range(1,M):
    dp[0][j] = dp[0][j-1]+arr[0][j]
for i in range(1,N):
    dp[i][0] = dp[i-1][0]+arr[i][0]
for i in range(1, N):
    for j in range(1, M):
        dp[i][j] = max(dp[i-1][j]+arr[i][j],dp[i][j-1]+arr[i][j],dp[i-1][j-1]+arr[i][j])
print(dp[N-1][M-1])