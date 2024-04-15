import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N,M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[-100000]*(M) for _ in range(N)]
dp[0][0] = arr[0][0]
for j in range(1, M):
    dp[0][j] = arr[0][j]+dp[0][j-1]

for i in range(1, N):
    left = [-10000] * M
    right = [-10000] * M
    for j in range(M):
        if j == 0:
            left[j] = dp[i-1][j] + arr[i][j]
        else:
            left[j] = max(arr[i][j]+left[j-1], dp[i-1][j]+arr[i][j])
    for j in range(M-1, -1, -1):
        if j == M-1:
            right[j] = dp[i-1][j] + arr[i][j]
        else:
            right[j] = max(arr[i][j] + dp[i-1][j], right[j+1] + arr[i][j])
    for j in range(M):
        dp[i][j] = max(right[j], left[j])
print(dp[-1][-1])