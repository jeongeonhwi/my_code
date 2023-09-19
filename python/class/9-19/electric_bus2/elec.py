import sys
sys.stdin = open('input.txt', 'r')




def battery(start, end, batt, cnt):
    global min_v
    if batt >= (end-start):
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
        for j in range(len(arr)):




T = int(input())
for tc in range(1, T+1):
    arr2 = list(map(int, input().split()))
    N, *arr = arr2
    p = [0]*(N-1)
    min_v = N*100
    battery(0, N-1, arr[0], 0)
    print(f'#{tc} {min_v}')