import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline



di = [1, -1, 0, 0, 1, -1, 1, -1]
dj = [0, 0, 1, -1, 1, 1, -1, -1]
N = int(input())
arr = [input() for _ in range(N)]
arr_open = [input() for _ in range(N)]
ans = [[0]*N for _ in range(N)]
check = False
for i in range(N):
    for j in range(N):
        if arr_open[i][j] != 'x':
            ans[i][j] = '.'
            continue
        if arr[i][j] == '*':
            check = True
        cnt = 0
        for k in range(8):
            ni,nj = i+di[k], j+dj[k]
            if 0<=ni<N and 0<=nj<N:
                if arr[ni][nj] == '*':
                    cnt += 1
        ans[i][j] = cnt
if check:
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '*':
                ans[i][j] = '*'
for i in ans:
    for j in i:
        print(j, end='')
    print()