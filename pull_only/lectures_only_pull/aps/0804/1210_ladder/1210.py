import sys
sys.stdin = open('input.txt')

T = 10
for _ in range(1, T+1):
    tc = int(input())
    N = 100
    arr = [list(map(int, input().split())) for _ in range(N)]
    # ----- 준비 끝

    # 1. 가장 끝에서 2를 찾는다!
    # 2. 찾은 2에서 부터 출발하여 사다리를 올라온다.
    # 3. 가장 처음으로 도착하면 해당 좌표를 반환한다.

    # 2 를 찾자!!
    col = 0
    for c in range(N):
        if arr[N-1][c] == 2:
            col = c
            break
    # print(col)

    # 사다리를 올라가자!!
    # 좌, 우, 상
    dr = [0, 0, -1]
    dc = [-1, 1, 0]
    row = N - 1

    # 횟수를 특정할 수 없어서 while 로 반복
    # row == 0 의 의미는 처음 시작 지점!
    # 그래서 시작 지점 아래에 있을 때는 계속 반복하여 이동
    while row > 0:
        # 이동
        dN = len(dr)
        for d_idx in range(3):
            # 다음 좌표 = 현재 위치 + 델타값
            nr = row + dr[d_idx]
            nc = col + dc[d_idx]

            # 유효한 범위 인지 가장 먼저 확인!!!
            # 그리고 이동 가능한 곳인지 확인!!
            if (0 <= nr < N) and (0 <= nc < N) and (arr[nr][nc] == 1):
                # 범위 내이고 이동이 가능하면 이동!!
                # 현재 위치 = 다음 좌표 갱신
                # 교착 상태가 발생!!
                    # 오른쪽(왼쪽) 이동하면
                    # 그 다음 순서에서 왔었던 곳을 다시 체크
                # 해결 방법
                    # 왔던 곳을 표시해두자
                    # 내가 지나왔던 곳의 값을 1이 아닌 다른 값
                arr[row][col] = 99  # 1이 아닌 값을 넣어서 지나왔다는 흔적을 남김
                row = nr
                col = nc
                break
    # 3. 좌표를 반환
    print(f'#{tc} {col}')


