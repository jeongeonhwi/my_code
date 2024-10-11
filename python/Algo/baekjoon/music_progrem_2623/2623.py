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

        stack.append(node)

        for a in arr[node]:
            if visited[a] == 0:
                dfs(a)



N,M = map(int, input().split())
arr = {i:set() for i in range(N + 1)}
for _ in range(M):
    data = list(map(int, input().split()))
    for i in range(len(data)-1):
        for j in range(i+1, len(data)):
            arr[data[i]].add(data[j])
print(arr)