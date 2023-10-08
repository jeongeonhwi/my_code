import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline


from heapq import heappop,heappush
def dfs():
    visited = [[[int(2e9)]*M for _ in range(N)] for _ in range(2)]
    hq = [(1,0,0,0)]
    visited[0][0][0] = 1
    while hq:
        cnt, i,j,w = heappop(hq)
        if visited[w][i][j] < cnt:
            continue
        for k in range(4):
            ni,nj = i+di[k],j+dj[k]
            if 0<=ni<N and 0<=nj<M and arr[ni][nj] == '0':
                if visited[w][ni][nj] <= cnt+1:
                    continue
                visited[w][ni][nj] = cnt+1
                heappush(hq, (cnt+1,ni,nj,w))
            else:
                if 0<=ni<N and 0<=nj<M and arr[ni][nj] == '1' and w == 0:
                    if visited[w+1][ni][nj] <= cnt+1:
                        continue
                    visited[w][ni][nj] = cnt+1
                    heappush(hq, (cnt+1,ni,nj,w+1))
    return min(visited[0][N-1][M-1], visited[1][N-1][M-1])




di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
N, M = map(int, input().split())
arr = [input() for _ in range(N)]
ans = dfs()
if ans == int(2e9):
    ans = -1
print(ans)