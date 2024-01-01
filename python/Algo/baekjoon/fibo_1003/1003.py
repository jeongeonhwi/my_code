import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    dp = [0]*41
    dp[0] = (1,0)
    dp[1] = (0,1)
    if N >= 2:
        for i in range(2,N+1):
            dp[i] = (dp[i-1][0]+dp[i-2][0],dp[i-1][1]+dp[i-2][1])
    print(*dp[N])