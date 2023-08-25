T = int(input()) # 백돌 2, 흑돌 1
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0]*N for _ in range(N)]

    # 기본돌 올리기
    n = N//2
    arr[n][n] = 2
    arr[n-1][n-1] = 2
    arr[n-1][n] = 1
    arr[n][n-1] = 1

    for _ in range(12):
        r, c ,color = map(int, input().split())
        row = r-1
        col = c-1
        arr[row][col] = color


        for dr, dc in [[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]:
            nr, nc = row + dr, col + dc
            point = []
            if 0 <= nr < N and 0 <= nc < N:
                while arr[nr][nc] != color:
                    if arr[nr][nc] == 0:
                        break
                    elif arr[nr][nc] != color:
                        point.append((nr,nc))
                    elif arr[nr][nc] == color:

                        for a, b in point:
                            arr[a][b] = color
                        nr, nc = nr+dr, nc+dc
                        break


    count = 0
    count2 = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                count += 1
            elif arr[i][j] == 2:
                count2 += 1

    print(f'#{tc} {count} {count2}')

