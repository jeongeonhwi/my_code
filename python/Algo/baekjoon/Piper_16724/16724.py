import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline


def dfs(si,sj):
    global label, safety_zone
    stack = [[si,sj]]
    visited[si][sj] = label
    while stack:
        i,j = stack.pop()
        ni,nj = move(i,j)
        if visited[ni][nj] == 0:
            visited[ni][nj] = label
            stack.append([ni,nj])
        elif visited[ni][nj] == label:
            label += 1
            safety_zone += 1
            return
        else:
            label += 1
            return


def move(i,j):
    di,dj = direct[arr[i][j]]
    return i+di,j+dj

N,M = map(int, input().split())
arr = [input().strip() for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
direct = {"U":(-1,0), "D":(1,0), "L":(0,-1), "R":(0,1)}
label = 1
safety_zone = 0
for i in range(N):
    for j in range(M):
        if visited[i][j] == 0:
            dfs(i,j)
print(safety_zone)