import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

def dfs(start):
    visited[start] = 1
    stack = [start]
    while stack:
        i = stack.pop()
        for j in arr[i]:
            if visited[j] == 0:
                visited[j] = 1
                stack.append(j)


N, M = map(int, input().split())
arr = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[a-1].append(b-1)
    arr[b-1].append(a-1)
visited = [0] * N
cnt = 0
for i in range(N):
    if visited[i] == 0:
        dfs(i)
        cnt += 1
print(cnt)