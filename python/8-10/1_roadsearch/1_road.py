import sys
sys.stdin = open('input.txt')

def dfs(n, V, adj_arr):
    stack = []
    visit = [0]*100
    visit[n] = 1
    while True:
        for w in range(V):
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
    if visit[99] == 1:
        return 1
    else:
        return 0



for _ in range(10):
    N, V = map(int, input().split())
    arr = list(map(int, input().split()))
    start = 0
    end = 99
    adj_arr = [[0]*100 for _ in range(100)]
    for i in range(len(arr)//2):
        adj_arr[arr[i*2]][arr[i*2+1]] = 1

    print(f'#{N} {dfs(start, 100, adj_arr)}')
