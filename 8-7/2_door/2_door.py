import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    # print(arr)
    result = []
    if M%2 == 0:
        for i in range(N):
            for j in range(N-M+1):
                total = []
                for k in range(M//2):
                    if arr[i][j+k] == arr[i][j+M-1-k]:
                        total.append(arr[i][j+k])
                for p in range(len(total)-1, -1, -1):
                    total.append(total[p])
                if len(total) == M:
                    result.append(total)
        for j in range(N):
            for i in range(N-M+1):
                total = []
                for k in range(M//2):
                    if arr[i+k][j] == arr[i+M-1-k][j]:
                        total.append(arr[i+k][j])
                for p in range(len(total)-1, -1, -1):
                    total.append(total[p])
                if len(total) == M:
                    result.append(total)
    else:
        for i in range(N):
            for j in range(N-M+1):
                total = []
                for k in range(M//2):
                    if arr[i][j+k] == arr[i][j+M-1-k]:
                        total.append(arr[i][j+k])
                total.append(arr[i][j + M // 2])
                for p in range(len(total)-2, -1, -1):
                    total.append(total[p])
                if len(total) == M:
                    result.append(total)
        for j in range(N):
            for i in range(N-M+1):
                total = []
                for k in range(M//2):
                    if arr[i+k][j] == arr[i+M-1-k][j]:
                        total.append(arr[i+k][j])
                total.append(arr[i + M // 2][j])
                for p in range(len(total)-2, -1, -1):
                    total.append(total[p])
                if len(total) == M:
                    result.append(total)
    result2 = result[0]
    print(f'#{tc}', end=' ')
    for i in result2:
        print(i, end='')
    print()