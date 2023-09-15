import sys
sys.stdin = open('input.txt', 'r')


def dfs(one, two, arr):
    visited = [0]*(N+1)
    stack = [one]
    visited[one] = 1
    while stack:
        i = stack.pop()
        if i == two:
            return visited[i]
        for j in range(N+1):
            if arr[i][j] == 1 and visited[j] == 0:
                stack.append(j)
                visited[j] = visited[i] + 1
    return -1


N = int(input())
one, two = map(int, input().split())
M = int(input())
arr = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    i, j = map(int, input().split())
    arr[i][j] = 1
    arr[j][i] = 1
ans = dfs(one, two, arr)
if ans != -1:
    ans -= 1
print(ans)