import sys
sys.stdin = open('input.txt', 'r')


def permutation(start, end, total):
    global min_v
    if total > min_v:
        return
    if start == end:
        min_v = min(total, min_v)
        return
    else:
        for j in range(N):
            if used[j] == 0:
                p[start] = number[j]
                used[j] = 1
                total2 = total + arr[start][number[j]]
                permutation(start+1, end, total2)
                used[j] = 0




T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    number = [i for i in range(N)]
    p = [0]*N
    used = [0]*N
    min_v = 1000000000000000
    permutation(0, N, 0)
    print(f'#{tc} {min_v}')