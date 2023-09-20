import sys
sys.stdin = open('input.txt', 'r')


def battery(start, end, batt, cnt):
    global min_v
    if min_v <= cnt:
        return
    if start == end:
        min_v = min(cnt, min_v)
        return
    else:
        battery(start + 1, end, arr[start]-1, cnt + 1)
        if batt > 0:
            battery(start + 1, end, batt - 1, cnt)


T = int(input())
for tc in range(1, T + 1):
    arr2 = list(map(int, input().split()))
    N, *arr = arr2
    arr += [0]
    min_v = N
    battery(1, N-1, arr[0]-1, 0)
    print(f'#{tc} {min_v}')