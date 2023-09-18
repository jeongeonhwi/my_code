import sys
sys.stdin = open('input.txt', 'r')


from collections import deque

def find_beaver(arr):
    for i in range(R):
        for j in range(C):
            if arr[i][j] == 'D':
                return [i,j]

def find_S(arr):
    for i in range(R):
        for j in range(C):
            if arr[i][j] == 'S':
                return [i,j]



def bfs(start, arr):
    visited = [[0]*C for _ in range(R)]
    a, b = start
    visited[a][b] = 1
    q = [start]
    q = deque(q)
    water = 1
    while q:
        i, j = q.popleft()
        if arr[i][j] == 'D':
            return visited[i][j]-1
        for k in range(4):
            ni, nj = i+di[k], j+dj[k]
            if 0<=ni<R and 0<=nj<C and arr[ni][nj] != 'X' and visited[ni][nj] == 0 and arr[ni][nj] != '*':
                visited[ni][nj] = visited[i][j]+1
                q.append((ni,nj))
                if water != visited[ni][nj]:
                    water = visited[ni][nj]
                    stack = []
                    for ii in range(R):
                        for jj in range(C):
                            if arr[ii][jj] == '*':
                                stack.append((ii,jj))
                    while stack:
                        ii,jj = stack.pop()
                        for kk in range(4):
                            nni, nnj = ii+di[kk], jj+dj[kk]
                            if 0<=nni<R and 0<=nnj<C and arr[nni][nnj] != 'X' and arr[nni][nnj] != 'D':
                                arr[nni][nnj] = '*'
                    if arr[ni][nj] == '*':
                        q.pop()
    return 'KAKTUS'




di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]
R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
beaver = find_beaver(arr)
S = find_S(arr)
ans = bfs(S, arr)
print(ans)