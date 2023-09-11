#피보나치수열 가장 효과적인방법
def fibo(n):
    dp = [0]*(n+1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n+1):
        dp[i]= dp[i-1] + dp[i-2]
    return dp[n]

dp = [0]*(100+1)
dp[0]=0
dp[1]=1
for i in range(2, 101):
    dp[i] = dp[i - 1] + dp[i - 2]
print(fibo(100))