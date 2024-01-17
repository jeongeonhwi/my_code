import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

row = input().strip()
col = input().strip()
dp = [[0]*len(col) for _ in range(len(row))]
if row[0] == col[0]:
    dp[0][0] = 1
for j in range(1,len(col)):
    if dp[0][j-1] == 1 or row[0] == col[j]:
        dp[0][j] = 1
for i in range(1,len(row)):
    if dp[i-1][0] == 1 or row[i] == col[0]:
        dp[i][0] = 1
for i in range(1,len(row)):
    for j in range(1,len(col)):
        if row[i] == col[j]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])

print(dp[-1][-1])