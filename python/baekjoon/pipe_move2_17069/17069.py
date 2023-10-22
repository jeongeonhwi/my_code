import sys
sys.stdin = open('input.txt', 'r')



def dfs(m, now):
    global cnt
    if now[0] < 0 and now[1] < 0:
        return
    if now[0] == N-1 and now[1] == N-1:
        cnt+=1
        visited[m][now[0]][now[1]] = 1
        return
    for mm in dir[m]:
        i,j = move[mm]
        ni,nj = now
        ni,nj = ni+i,nj+j
        if mm == 0 or mm == 2:
            if 0<=ni<N and 0<=nj<N and arr[ni][nj] == 0:
                if visited[mm][ni][nj]:
                    cnt+=1+visited[mm][ni][nj]
                    visited[m][now[0]][now[1]] = 1+visited[mm][ni][nj]
                    return
                dfs(mm, (ni,nj))
        else:
            if 0<=ni<N and 0<=nj<N and arr[ni][nj] == 0 and arr[ni-1][nj] == 0 and arr[ni][nj-1] == 0:
                if visited[mm][ni][nj]:
                    cnt+=1
                    visited[m][now[0]][now[1]] = 1+visited[mm][ni][nj]
                    return
                dfs(mm, (ni,nj))

# 가로 : 0 대각선 : 1 세로 : 2
dir = {
    0:(0,1),
    1:(0,1,2),
    2:(1,2),
}
#          가로 대각선 세로
move = [(0,1), (1,1), (1,0)]
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[[0]*N for _ in range(N)] for _ in range(3)]
visited[0][0][1] = 1
cnt = 0
dfs(0, (0,1))
print(cnt)