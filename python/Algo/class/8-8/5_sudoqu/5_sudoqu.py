import sys
sys.stdin = open('input.txt')
import copy

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    # 가로 세로 표를 나눠서 세번씩 포문을 돌려 조건을 만족시키자.
    # lose point
    lpoint = 0
    # 가로를 버블정렬을 이용하여 같은값이 있는지 확인
    width = copy.deepcopy(arr)
    for k in range(9):
        for i in range(9, 0, -1):
            for j in range(1, i):
                if width[k][j] < width[k][j-1]:
                    width[k][j], width[k][j-1] = width[k][j-1], width[k][j]
                elif width[k][j] == width[k][j-1]:
                    lpoint += 1
                    break
    # 세로
    if lpoint == 0:
        length = copy.deepcopy(arr)
        for k in range(9):
            for i in range(9, 0, -1):
                for j in range(1, i):
                    if length[j][k] < length[j-1][k]:
                        length[j][k], length[j-1][k] = length[j-1][k], length[j][k]
                    elif length[j][k] == length[j-1][k]:
                        lpoint += 1
                        break
    # 구획별로
    if lpoint == 0:
        sector = copy.deepcopy(arr)
        seclist = []
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                for di in range(3):
                    for dj in range(3):
                        seclist.append(sector[i+di][j+dj])
                for ni in range(9, 0, -1):
                    for nj in range(1, ni):
                        if seclist[nj] < seclist[nj-1]:
                            seclist[nj], seclist[nj-1] = seclist[nj-1], seclist[nj]
                        elif seclist[nj] == seclist[nj-1]:
                            lpoint += 1
                            break
    result = 0
    if lpoint > 0:
        result = 0
    else:
        result += 1
    print(f'#{tc} {result}')
