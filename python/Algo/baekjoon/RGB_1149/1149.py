import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
dp = [[0]*3 for _ in range(N)]
for i in range(N):
    if i == 0:
        data = list(map(int, input().split()))
        dp[i][0] = data[0]
        dp[i][1] = data[1]
        dp[i][2] = data[2]
    else:
        data = list(map(int, input().split()))
        dp[i][0] = min(data[0]+dp[i-1][1], data[0]+dp[i-1][2])
        dp[i][1] = min(data[1]+dp[i-1][0], data[1]+dp[i-1][2])
        dp[i][2] = min(data[2]+dp[i-1][0], data[2]+dp[i-1][1])
print(min(dp[-1]))
