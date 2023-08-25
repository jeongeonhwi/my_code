import sys
sys.stdin = open('input.txt', 'r')

di = [1, -1, 0, 0, -1, -1, 1, 1]
dj = [0, 0, 1, -1, 1, -1, -1, 1]


T= int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    result = False
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                for k in range(8):
                    i_idx = i
                    j_idx = j
                    count = 1
                    while True:
                        ni = i_idx + di[k]
                        nj = j_idx + dj[k]
                        if count == 5:
                            result = True
                            break
                        if 0<=ni<N and 0<=nj<N:
                            if arr[ni][nj] == 'o':
                                count += 1
                                i_idx = ni
                                j_idx = nj
                            else:
                                break
                        else:
                            break
    if result:
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')