import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ninelist = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            ninelist[i][j] = arr[N-1-j][i]
    twoninelist = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            twoninelist[i][j] = arr[N-1-i][N-1-j]
    threeninelist = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            threeninelist[i][j] = arr[j][N-1-i]
    # print(ninelist)
    # print(twoninelist)
    # print(threeninelist)
    print(f'#{tc}')
    for i in range(N):
        for j in range(N):
            print(ninelist[i][j], end="")
        print(' ', end="")
        for j in range(N):
            print(twoninelist[i][j], end="")
        print(' ', end="")
        for j in range(N):
            print(threeninelist[i][j], end="")
        print()
