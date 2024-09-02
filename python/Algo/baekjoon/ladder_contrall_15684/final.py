import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(step, i,j, start):
    global ans, flag
    if step > 3:
        return
    if i >= H:
        if j == start:
            dfs(step, 0,j+1, start+1)
        return
    if i == 0 and start >= N:
        ans = step
        return
    dfs(step, i + 1, j+arr[i][j], start)
    if check_left(i,j):
        dfs(step+1, i+1,j-1, start)
        arr[i][j - 1], arr[i][j] = 0, 0
    if check_right(i,j):
        dfs(step+1, i+1,j+1, start)
        arr[i][j], arr[i][j + 1] = 0, 0


def check_left(i,j):
    if arr[i][j] != 0:
        return False
    if j == 0:
        return False
    if arr[i][j-1] != 0:
        return False
    arr[i][j-1], arr[i][j] = 1, -1
    return True

def check_right(i,j):
    if arr[i][j] != 0:
        return False
    if j == N-1:
        return False
    if arr[i][j+1] != 0:
        return False
    arr[i][j], arr[i][j+1] = 1, -1
    return True


N,M,H = map(int, input().split())
arr = [[0]*N for _ in range(H)]
for _ in range(M):
    i,j = map(int, input().split())
    i,j = i-1,j-1
    arr[i][j] = 1
    arr[i][j+1] = -1
ans = -1
dfs(0,0,0,0)
print(ans)
