from heapq import heappush, heappop

def find_s_e(board):
    s,e = 0,0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                s = (i,j)
            if board[i][j] == 'G':
                e = (i,j)
    return (s,e)

def bfs(si,sj,N,M,board):
    direction = {1:(0,1), 2:(0,-1), 3:(1,0), 4:(-1,0)}
    visited = [[float('inf')]*M for _ in range(N)]
    q = [(0,si,sj)]
    visited[si][sj] = 0
    while q:
        c,i,j = heappop(q)
        print(c,i,j,board[i][j])
        if visited[i][j] < c:
            continue
        for d in [(0,1),(0,-1),(1,0),(-1,0)]:
            ni,nj = i+d[0], j+d[1]
            while True:
                if 0<=ni<N and 0<=nj<M:
                    if board[ni][nj] == 'D':
                        if board[ni-d[0]][nj-d[1]] == 'G':
                            return c+1
                        if visited[ni-d[0]][nj-d[1]] <= c+1:
                            break
                        visited[ni-d[0]][nj-d[1]] = c+1
                        heappush(q, (c+1,ni-d[0],nj-d[1]))
                        break
                else:
                    if visited[ni-d[0]][nj-d[1]] <= c+1:
                        break
                    visited[ni-d[0]][nj-d[1]] = c+1
                    heappush(q, (c+1,ni-d[0],nj-d[1]))
                    break
                ni,nj = ni+d[0], nj+d[1]

    return -1

board = ['...','..R','..G']
answer = 0
N = len(board)
M = len(board[0])
start, end = find_s_e(board)
answer = bfs(start[0],start[1],N,M,board)
print(answer)