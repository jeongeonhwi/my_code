import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
if N == 0:
    print(0)
    exit()
health = list(map(int, input().split()))
happyness = list(map(int, input().split()))

dp = [[0]*N for _ in range(100)]
for i in range(100):
    if i >= health[0]:
        dp[i][0] = happyness[0]
for j in range(N):
    if health[j] == 0:
        dp[0][j] = happyness[j]
for j in range(1,N):
    j_health = health[j]
    j_happyness = happyness[j]
    for i in range(1, 100):
        if i >= j_health:
            dp[i][j] = max(dp[i-j_health][j-1] + j_happyness, dp[i][j-1])
        else:
            dp[i][j] = dp[i][j-1]
print(dp[-1][-1])