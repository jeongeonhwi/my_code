import sys
sys.stdin = open('input.txt', 'r')

# 로봇은 왼쪽 오른쪽 아래쪽으로 이동가능,
# 한번 탐사한 지역은 탐사하지 않음
# 탐사지역은 가치가 존재, 가치의 합이 최대가 되도록 하는 프로그램을 작성

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*M for _ in range(N)]
dp[0][0] = arr[0][0]
tmpdp = [[0]*M for _ in range(N)]
for i in range(1,M):
    dp[0][i] = arr[0][i]+dp[0][i-1]
# for i in range(1,N):
#     dp[i][0] = arr[i][0] + dp[i-1][0]
# for i in dp:
#     print(i)
for i in range(1,N):
    for j in range(M):
        dp[i][j] = arr[i][j] + dp[i-1][j]
    for j in range(M):
        for right in range(j+1,M):
            dp[i][right] = max(dp[i][right-1]+arr[i][right],dp[i][right])
        for left in range(j-1,-1,-1):
            tmpdp[i][left] = max(max(dp[i][left+1]+arr[i][left], dp[i][left]), tmpdp[i][left])
    for j in range(M):
        dp[i][j] = max(dp[i][j], tmpdp[i][j])
for i in dp:
    print(i)