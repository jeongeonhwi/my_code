def find_i():
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'I':
                return i, j


def dfs(si, sj):
    visited = [[0] * m for _ in range(n)]
    stack = [(si, sj)]
    visited[si][sj] = 1
    mp = 0
    while stack:
        i, j = stack.pop()
        for ni, nj in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1), ]:
            if 0 <= ni < n and 0 <= nj < m and visited[ni][nj] == 0 and arr[ni][nj] != 'X':
                visited[ni][nj] = 1
                stack.append((ni, nj))
                if arr[ni][nj] == 'P':
                    mp += 1
    return mp


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
pi, pj = find_i()
ans = dfs(pi, pj)
if ans == 0:
    print('TT')
else:
    print(ans)