import sys
sys.stdin = open('input.txt')

def bfs(S, G, arr):
    visited = [0]*(V+2)
    q = []
    q.append(S)
    visited[S] = 1
    while q:
        i = q.pop(0)
        if i == G:
            return visited[i]-1
        for k in range(V+2):
            if arr[i][k] == 1 and visited[k] == 0:
                q.append(k)
                visited[k] = visited[i] + 1
    return 0

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = [[0]*(V+2) for _ in range(V+2)]
    for _ in range(E):
        i, j = map(int, input().split())
        arr[i][j] = 1
        arr[j][i] = 1
    S, G = map(int, input().split())
    # print(arr)
    ans = bfs(S, G, arr)
    print(f'#{tc} {ans}')
