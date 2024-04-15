import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]


dp = [[0]*(T+1) for _ in range(N+1)]

for i in range(1,N+1):
    study, cost = arr[i-1]
    for j in range(1,T+1):
        if j >= study:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-study]+cost)

        else:
            dp[i][j] = dp[i-1][j]


print(dp[N][T])