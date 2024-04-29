import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
dp = [0]*N
for i in range(N):
    dp[i] = 1
    for j in range(i):
        if arr[j] > arr[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(N-max(dp))