import sys
sys.stdin = open('input.txt', 'r')



import copy

def permutation(start, end, total):
    global min_v
    global max_v
    if start == end:
        # print(p)
        min_v = min(min_v, total)
        idx = 0
        x = 1
        for i in arr:
            x *= i[p[idx]] / 100
            idx += 1
        max_v = max(max_v, x * 100)
        return

    if total > min_v:
        return
    else:
        for j in range(N):
            if used[j] == 0:
                p[start] = num[j]
                used[j] = 1
                total2 = total + fail[start][p[start]]
                permutation(start + 1, end, total2)
                used[j] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    fail = copy.deepcopy(arr)
    for i in range(N):
        for j in range(N):
            fail[i][j] = 100 - fail[i][j]
    num = [i for i in range(N)]
    # print(fail)
    used = [0] * N
    p = [0] * N
    min_v = 1000000000000000000000000000
    max_v = 0
    permutation(0, N, 0)
    min_v = 100 - min_v
    print(f'#{tc}', end=' ')
    print('%.6f' % max_v)