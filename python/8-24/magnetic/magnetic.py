import sys
sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')
# 1은 N극 2는 S극 테이블 윗부분에는 N 테이블 아랫부분에는 S
T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    fake = [[0]*N for _ in range(N)]
    for j in range(N):
        for i in range(N):
            fake[j][i] = arr[i][j]

    count = 0
    for i in range(N):
        color = 0
        for j in range(N):
            if color == 0 and fake[i][j] == 2:
                fake[i][j] = 0
            elif color == 0 and fake[i][j] == 1:
                color = 1
            elif color == 1 and fake[i][j] == 2:
                count += 1
                color = 2
            elif color == 2 and fake[i][j] == 1:
                color = 1
    print(f'#{tc} {count}')