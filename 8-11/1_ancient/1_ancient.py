import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    count = 0
    for i in range(N):
        total = 0
        for j in range(M):
            if arr[i][j] == 1:
                total += 1
            elif arr[i][j] == 0:
                total = 0
            if total > count:
                count = total

    for j in range(M):
        total = 0
        for i in range(N):
            if arr[i][j] == 1:
                total += 1
            elif arr[i][j] == 0:
                total = 0
            if total > count:
                count = total
    print(f'#{tc} {count}')