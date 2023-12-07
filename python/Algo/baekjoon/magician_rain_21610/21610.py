import sys
sys.stdin = open('input.txt', 'r')


#무조건 비바라기 위치는 (N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)
# 방향은 0부터 순서대로 (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)

import copy
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cloud = {(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)}
direction = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
direction2 = [(-1, -1), (-1, 1), (1, 1), (1, -1)]
for _ in range(M):
    d, s = map(int, input().split())
    # s를 한번에 이동하기
    cloud4 = set()
    for i in cloud:
        ai = i[0]+direction[d-1][0]*s
        aj = i[1]+direction[d-1][1]*s
        if ai < 0:
            ai = N-((-ai)%N)
        if ai > N-1:
            ai = ai%N
        if aj < 0:
            aj = N-((-aj)%N)
        if aj > N-1:
            aj = aj%N
        if ai > N-1:
            ai = ai%N
        cloud4.add((ai,aj))
        # print(a, b)
    # 클라우드 아래 1씩 증가
    cloud = copy.deepcopy(cloud4)
    for i,j in cloud:
        arr[i][j] += 1
    # 대각선 검사
    for i,j in cloud:
        for di, dj in direction2:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N and arr[ni][nj] > 0:
                arr[i][j] += 1
    cloud2 = set()
    for i in range(N):
        for j in range(N):
            if (i, j) not in cloud:
                if arr[i][j] >= 2:
                    arr[i][j] -= 2
                    cloud2.add((i,j))
    cloud = copy.deepcopy(cloud2)
cnt = 0
for i in arr:
    cnt += sum(i)
print(cnt)