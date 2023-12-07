import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    min_v = 100000000000
    for i in range(1, 1<<N):
        group = []
        for j in range(N):
            if i&(1<<j):
                group.append(arr[j])
        tmp = sum(group)
        if tmp >=B:
            if min_v > tmp-B:
                min_v = tmp-B
    print(f'#{tc} {min_v}')