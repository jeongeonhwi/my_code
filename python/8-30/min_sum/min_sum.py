import sys
sys.stdin = open('input.txt', 'r')

def suneol(i, n, a, b):
    global min_v
    ss = sum(p[:i])
    if ss>= min_v:
        return
    if i == n:
        min_v = sum(p)
    else:
        for j in range(n):
            if used[j] == 0:
                p[i] = arr[a+di[direct[j]]][b+dj[direct[j]]]
                used[j] = 1
                suneol(i + 1, n, a, b)
                used[j] = 0
                print(p)


di = [0, 1]
dj = [1, 0]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    n = 2 * (N - 1)
    used = [0] * (n)
    p = [0] * (n)
    min_v = 10000000000
    s = 0
    a = 0
    b = 0
    direct = [1] * (N - 1) + [0] * (N - 1)
    suneol(0, n, a, b)
    print(f'#{tc} {min_v}')