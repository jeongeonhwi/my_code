import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

# 로봇은 왼쪽 오른쪽 아래쪽으로 이동가능,
# 한번 탐사한 지역은 탐사하지 않음
# 탐사지역은 가치가 존재, 가치의 합이 최대가 되도록 하는 프로그램을 작성

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[-101]*M for _ in range(N)]
dp[0][0] = arr[0][0]
tmpdp = [[-101]*M for _ in range(N)]
for i in range(1,M):
    dp[0][i] = arr[0][i]+dp[0][i-1]
for i in range(1,N):
    for j in range(M):
        dp[i][j] = arr[i][j] + dp[i-1][j]
    for j in range(M):
        now = dp[i][j]
        idx = j+1
        while idx < M:
            now += arr[i][idx]
            tmpdp[i][idx] = max(tmpdp[i][idx], now)
            idx+=1
        now = dp[i][j]
        idx = j - 1
        while idx >= 0:
            now += arr[i][idx]
            tmpdp[i][idx] = max(tmpdp[i][idx], now)
            idx-=1
    for j in range(M):
        dp[i][j] = max(dp[i][j], tmpdp[i][j])
print(dp[N-1][M-1])