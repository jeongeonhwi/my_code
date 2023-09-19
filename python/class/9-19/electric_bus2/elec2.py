import sys
sys.stdin = open('input.txt', 'r')


def battery(start, end, batt, cnt):
    global min_v
    if batt >= (end - start):
        min_v = min(cnt, min_v)
        return
    if min_v < cnt:
        return
    if batt < 0:
        return
    if start == end:
        if batt < 0:
            return
        min_v = min(cnt, min_v)
        return
    else:
        if batt == 0:
            battery(start + 1, end, batt - 1, cnt)
        else:
            battery(start + 1, end, arr[start], cnt + 1)
            battery(start + 1, end, batt - 1, cnt)


T = int(input())
for tc in range(1, T + 1):
    arr2 = list(map(int, input().split()))
    N, *arr = arr2
    min_v = N * 100
    battery(2, N, arr[1]-1, 0)
    print(f'#{tc} {min_v}')
