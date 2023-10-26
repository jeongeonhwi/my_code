import sys
sys.stdin = open('input.txt', 'r')


N = int(input())
arr = [int(input()) for _ in range(N)]
dp = [0]*N
p = -1
while True:
    if p >= N-3:
        if p == N -3:

    p+=3
    tmp1 = arr[p-2]+arr[p-1]
    tmp2 = arr[p-2]+arr[p]
    dp[p] = max(tmp1, tmp2)
    if p == 2:
        continue
    dp[p] += dp[p-3]