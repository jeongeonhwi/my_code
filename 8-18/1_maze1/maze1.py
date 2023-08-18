import sys
sys.stdin = open('input.txt')

def bfs(sti, stj):
    visited = [[0]*16 for _ in range(16)]
    q = []
    q.append((sti, stj))
    visited[sti][stj] = 1
    while q:
        i, j = q.pop(0)
        if arr[i][j] == 3:
            return 1
        for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            ni = i+di
            nj = j+dj
            if 0<=ni<16 and 0<=nj<16 and arr[ni][nj]!=1 and visited[ni][nj] ==0:
                q.append((ni, nj))
                visited[ni][nj] = 1
    return 0



T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(16)]
    sti, stj = 1, 1
    ans = bfs(sti, stj)
    print(f'#{tc} {ans}')