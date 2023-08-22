import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    arr = [0]*(N+1)
    for _ in range(M):
        num, val = map(int, input().split())
        arr[num] = val
    idx = N
    while idx>2:
        if idx//2 == (idx-1)//2 and arr[idx-1] != 0 and arr[idx] != 0:
            arr[idx//2] = arr[idx]+arr[idx-1]
            idx -= 2
        else:
            arr[idx//2] = arr[idx]
            idx -= 1
    print(f'#{tc} {arr[L]}')
