import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(8)]
    total = 0
    for i in range(8):
        for j in range(8-N+1):
            count = 0
            for k in range(N//2):
                if arr[i][j+k] == arr[i][j+N-1-k]:
                    count += 1
            if count == N//2:
                total += 1

    for j in range(8):
        for i in range(8-N+1):
            count = 0
            for k in range(N//2):
                if arr[i+k][j] == arr[i+N-1-k][j]:
                    count += 1
            if count == N//2:
                total += 1
    print(f'#{tc} {total}')