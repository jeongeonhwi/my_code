import sys
sys.stdin = open('input.txt')


def bfs(S, fake):
    visited = [0]*101
    q = []
    q.append(S)
    visited[S] = 1
    while q:
        i = q.pop(0)
        for k in range(len(visited)):
            if fake[i][k] == 1 and visited[k] == 0:
                q.append(k)
                visited[k] = visited[i] +1
    return visited


T = 10
for tc in range(1, T+1):
    N, S = map(int, input().split())
    arr = list(map(int, input().split()))
    fake = [[0]*101 for _ in range(101)]
    for i in range(len(arr)//2):
        fake[arr[i*2]][arr[i*2+1]] = 1
    print(arr)
    print(fake)
    alist = bfs(S, fake)
    max_v = 0
    for i in alist:
        if max_v < i:
            max_v = i
    result = []
    for i in range(len(alist)):
        if alist[i] == max_v:
            result.append(i)
    result.sort()
    ans = result[-1]
    print(f'#{tc} {ans}')