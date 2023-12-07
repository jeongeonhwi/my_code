import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

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
    lefttmp = arr[i][:]
    righttmp = arr[i][:]
    for j in range(M):
        if j == 0:
            lefttmp[j] += dp[i-1][j]
            continue
        lefttmp[j] += max(dp[i-1][j], lefttmp[j-1])
    for j in range(M-1, -1, -1):
        if j == M-1:
            righttmp[j] += dp[i-1][j]
            continue
        righttmp[j] += max(dp[i-1][j], righttmp[j+1])

    for j in range(M):
        dp[i][j] = max(lefttmp[j], righttmp[j])
print(dp[N-1][M-1])