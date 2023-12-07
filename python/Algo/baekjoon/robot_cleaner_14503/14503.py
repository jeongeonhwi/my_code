import sys
sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')


# 북 동 남 서
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
dlist = []
N, M = list(map(int, input().split()))
i, j, d = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
while True:
    if arr[i][j] == 0:
        arr[i][j] = 2
        cnt += 1
    for _ in range(4):
        if d != 0:
            d-= 1
        else:
            d = 3
        ni, nj = i+di[d], j+dj[d]
        if arr[ni][nj] == 0:
            arr[ni][nj] = 2
            cnt += 1
            i, j = ni, nj
            break
    else:
        i, j = i-di[d], j-dj[d]
        if arr[i][j] == 1:
            break
# for i in arr:
#     print(i)
print(cnt)
