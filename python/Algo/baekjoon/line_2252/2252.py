import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

def topology_sort():
    visited = [0]*(N+1)
    stack = []

    def dfs(node):
        if visited[node] == 1:
            return
        visited[node] = 1

        for a in arr[node]:
            dfs(a)

        stack.append(node)

    for n in range(1,N+1):
        if visited[n] == 0:
            dfs(n)
    return stack[::-1]



N,M = map(int, input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    pre, post = map(int, input().split())
    arr[pre].append(post)

print(*topology_sort())