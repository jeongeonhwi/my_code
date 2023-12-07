import sys
sys.stdin = open('input.txt', 'r')



# 가로 : 0 대각선 : 1 세로 : 2
dir = {
    0:(0,1),
    1:(0,1,2),
    2:(1,2),
}
#          가로 대각선 세로
move = [(0,1), (1,1), (1,0)]
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[[0]*N for _ in range(N)] for _ in range(3)]
visited[0][0][1] = 1
cnt = 0
for j in range(N):
    if arr[0][j] == 1:
        break
    visited[0][0][j] = 1
for i in range(1, N):
    for j in range(2, N):
        if arr[i][j] == 1:
            continue
        visited[0][i][j] = visited[0][i][j-1] + visited[1][i][j-1]
        visited[2][i][j] = visited[2][i-1][j] + visited[1][i-1][j]
        if arr[i-1][j] == 0 and arr[i][j-1] == 0:
            visited[1][i][j] = visited[0][i-1][j-1] + visited[2][i-1][j-1] + visited[1][i-1][j-1]
for c in range(3):
    cnt += visited[c][N-1][N-1]
# for t in visited:
#     for i in t:
#         print(i)
#     print()
print(cnt)