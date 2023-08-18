import sys
sys.stdin = open('input.txt')

def dfs(n, V, adj_arr):
    stack = []
    visit = [0]*(V+1)
    visit[n] = 1
    while True:
        for w in range(V+1):
            if adj_arr[n][w] == 1 and visit[w] == 0:
                stack.append(n)
                n = w
                visit[n] = 1
                break
        else:
            if stack:
                n = stack.pop()
            else:
                break
    return visit


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(E)]
    arrlist = []
    for i in range(len(arr)):
        for j in range(2):
            arrlist.append(arr[i][j])
    S, G = map(int, input().split())
    adj_arr = [[0]*(V+1) for _ in range(V+1)]
    for i in range(E):
        adj_arr[arrlist[i*2]][arrlist[i*2+1]] = 1
    result = dfs(S, V, adj_arr)
    print(result)
    if result[G] == 1:
        print(f'#{tc} {1}')
    else:
        print(f'#{tc} {0}')