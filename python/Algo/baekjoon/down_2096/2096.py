import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline


N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
max_dp, min_dp = [0,0,0], [10,10,10]

for i in range(1, N):
    now = max_dp[0] + arr[i][0]
    if now > max_dp[0]:
        max_dp[0] = now
    now = max_dp[0] + arr[i][1]
    if now > max_dp[1]:
        max_dp[1] = now

    now = max_dp[1] + arr[i][0]
    if now > max_dp[0]:
        max_dp[0] = now
    now = max_dp[1] + arr[i][1]
    if now > max_dp[1]:
        max_dp[1] = now
    now = max_dp[1] + arr[i][2]
    if now > max_dp[2]:
        max_dp[2] = now

    now = max_dp[2] + arr[i][1]
    if now > max_dp[1]:
        max_dp[1] = now
    now = max_dp[2] + arr[i][2]
    if now > max_dp[2]:
        max_dp[2] = now
    print(max_dp)
print(max(max_dp))