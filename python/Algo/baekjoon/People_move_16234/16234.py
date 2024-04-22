import copy
import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

def dfs(si,sj):
    stack = [(si,sj)]
    tmp_visited[si][sj] = [(si,sj)]
    while stack:
        i,j = stack.pop()
        for ni,nj in [(i+1,j),(i,j+1),(i-1,j),(i,j-1),]:
            if 0<=ni<N and 0<=nj<N and tmp_visited[ni][nj] == 0:
                if L<=abs(arr[ni][nj] - arr[i][j])<=R:
                    tmp_visited[ni][nj] = 1
                    tmp_visited[si][sj].append((ni,nj))
                    stack.append((ni,nj))


N,L,R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

visited = [[0]*N for _ in range(N)]
ans = 0
while True:
    tmp_visited = copy.deepcopy(visited)
    for i in range(N):
        for j in range(N):
            if tmp_visited[i][j] == 0:
                dfs(i,j)
    flag = 0
    for i in range(N):
        for j in range(N):
            if type(tmp_visited[i][j]) == list and len(tmp_visited[i][j]) > 1:
                sumdata = 0
                for ti,tj in tmp_visited[i][j]:
                    sumdata += arr[ti][tj]
                for ti,tj in tmp_visited[i][j]:
                    arr[ti][tj] = sumdata//len(tmp_visited[i][j])
            else:
                flag += 1
    if flag == N*N:
        break

    ans += 1

print(ans)