import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N,M = map(int, input().split())
activate = list(map(int, input().split()))
cost = list(map(int, input().split()))
min_v = sum(cost)+1
dp = [[0]*N for _ in range(sum(cost)+1)]
for i in range(sum(cost)+1):
    if i >= cost[0]:
        dp[i][0] = activate[0]
        if dp[i][0] >= M:
            min_v = min(min_v, cost[0])
for j in range(N):
    if cost[j] == 0:
        dp[0][j] = activate[j]
        if dp[0][j] >= M:
            min_v = min(min_v, cost[j])
for j in range(N):
    jc = cost[j]
    ja = activate[j]
    for i in range(sum(cost)+1):
        if jc > i:
            if j == 0:
                continue
            dp[i][j] = dp[i][j-1]
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-jc][j-1] + ja)
        if dp[i][j] >= M:
            min_v = min(min_v,i)
print(min_v)