import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]
dp = [0]*(N+1)
dp[0] = arr[0]
if N>1:
    dp[1] = dp[0] + arr[1]
    if N>2:
        dp[2] = max(dp[0]+arr[2], dp[1], arr[1]+arr[2])
        for i in range(3,N):
            dp[i] = max(arr[i]+arr[i-1]+dp[i-3], arr[i]+dp[i-2], dp[i-1])
        print(dp[N-1])
    else:
        print(dp[1])
else:
    print(dp[0])