import sys
sys.stdin = open('input.txt', 'r')

def dfs(one, arr):
    visited = [0]*(N+1)
    stack = [one]
    visited[one] = 1
    while stack:
        i = stack.pop()
        for j in range(N+1):
            if arr[i][j] == 1 and visited[j] == 0:
                stack.append(j)
                visited[j] = 1
                print(visited)
    result = visited.count(1)
    return result




N = int(input())
M = int(input())
arr = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    i, j = map(int, input().split())
    arr[i][j] = 1
    arr[j][i] = 1
ans = dfs(1, arr)
print(ans-1)