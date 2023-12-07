import sys
sys.stdin = open('input.txt')

def dfs(start, arr):
    visited = [0]*(N+1)
    stack = []
    stack.append(start)
    visited[start] = start
    print(start, end=' ')
    while stack:
        a = stack.pop()
        for i in range(1, N+1):
            if arr[a][i] != 0 and visited[i] == 0:
                stack.append(i)
                visited[i] = i
                print(i, end=' ')
                break
                
    return visited


def bfs(start, arr):
    visited = [0]*(N+1)
    q = []
    q.append(start)
    visited[start] = start
    while q:
        a = q.pop(0)
        print(a, end=' ')
        for j in range(1, N+1):
            if arr[a][j] != 0 and visited[j] == 0:
                q.append(j)
                visited[j] = a
    return


N, M, start = map(int, input().split())
arr = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1
    
dfs(start, arr)
print()
bfs(start, arr)
print()