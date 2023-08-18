import sys
sys.stdin = open('input.txt')

def bfs(sti, stj, arr):
    visited = [[0]*100 for _ in range(100)]
    q = []
    q.append((sti, stj))
    visited[sti][stj] = 1
    while q:
        i, j = q.pop(0)
        if arr[i][j] == 3:
            return 1
        for di, dj in [[1,0], [0,1], [-1,0], [0,-1]]:
            ni,nj = i+di, j+dj
            if 0<=ni<100 and 0<=nj<100 and arr[ni][nj] != 1 and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = 1

    return 0


T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(100)]
    sti,stj = 1, 1
    ans = bfs(sti, stj, arr)
    print(f'#{N} {ans}')