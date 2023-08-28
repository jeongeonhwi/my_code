import sys
sys.stdin = open('input.txt')

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

ddi = [-1, -1, 1, 1]
ddj = [-1, 1, -1, 1]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_v = 0
    for i in range(N):
        for j in range(N):
            total = 0
            total += arr[i][j]
            for k in range(4):
                for m in range(1, M):
                    ni = i+di[k]*m
                    nj = j+dj[k]*m
                    if 0<=ni<N and 0<=nj<N:
                        total += arr[ni][nj]
            if max_v <= total:
                max_v = total
            total = 0
            total += arr[i][j]
            for k in range(4):
                for m in range(1, M):
                    ni = i + ddi[k] * m
                    nj = j + ddj[k] * m
                    if 0 <= ni < N and 0 <= nj < N:
                        total += arr[ni][nj]
            if max_v <= total:
                max_v = total
    print(f'#{tc} {max_v}')