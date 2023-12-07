import sys
sys.stdin = open('input.txt')

di = [1, -1, 0, 0, 1, 1, -1, -1]
dj = [0, 0, 1, -1, 1, -1, 1, -1]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    fake = [[0]*N for _ in range(N)]
    fake[N//2-1][N//2-1] = 2
    fake[N//2][N//2-1] = 1
    fake[N//2-1][N//2] = 1
    fake[N//2][N//2] = 2
    for _ in range(M):
        jjj, iii, num = map(int, input().split())
        ii = iii-1
        jj = jjj-1
        fake[ii][jj] = num
        # print(fake)
        for k in range(8):
            ni = ii + di[k]
            nj = jj + dj[k]
            if 0<=ni<N and 0<=nj<N:
                if fake[ni][nj] != num and fake[ni][nj] != 0:
                    for i in range(1, 100):
                        nni = ii+di[k]*i
                        nnj = jj+dj[k]*i
                        try:
                            if fake[nni][nnj] != 0:
                                if fake[nni][nnj] == num:
                                    for j in range(1, i):
                                        nnni = ii + di[k] * j
                                        nnnj = jj + dj[k] * j
                                        fake[nnni][nnnj] = num
                                    break
                            else:
                                break
                        except:
                            pass
    B_count = 0
    W_count = 0
    for i in range(N):
        for j in range(N):
            if fake[i][j] == 1:
                B_count += 1
            elif fake[i][j] == 2:
                W_count += 1
    # print(fake)
    print(f'#{tc} {B_count} {W_count}')

