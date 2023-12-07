import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


from collections import deque
def dfs():
    visited = [[(float('inf'),wall+1)]*M for _ in range(N)]
    hq = [(1,0,0,0)]
    hq = deque(hq)
    visited[0][0] = (1,0)
    while hq:
        cnt, i,j,w = hq.popleft()
        if i == N-1 and j == M-1:
            return cnt
        if visited[i][j][0] < cnt and visited[i][j][1] <= w:
            continue
        for di,dj in [(0,1),(-1,0),(0,-1),(1,0)]:
            ni,nj = i+di,j+dj
            if 0<=ni<N and 0<=nj<M and arr[ni][nj] == '0':
                if visited[ni][nj][0] <= cnt+1 and visited[ni][nj][1] <= w:
                    continue
                visited[ni][nj] = (cnt+1,w)
                hq.append((cnt+1,ni,nj,w))
            else:
                if 0<=ni<N and 0<=nj<M and arr[ni][nj] == '1' and w < wall:
                    if visited[ni][nj][0] <= cnt+1 and visited[ni][nj][1] <= w+1:
                        continue
                    visited[ni][nj] = (cnt+1,w+1)
                    hq.append((cnt+1,ni,nj,w+1))
    return visited[N-1][M-1][0]




N, M, wall = map(int, input().split())
arr = [input() for _ in range(N)]
ans = dfs()
if ans == float('inf'):
    ans = -1
print(ans)