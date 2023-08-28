import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    heap = [0]*(N+1)
    last_idx = 1
    for i in range(N):
        if not heap[last_idx]:
            heap[last_idx] = arr[i]
        else:
            last_idx += 1
            heap[last_idx] = arr[i]
            chl = last_idx
            par = chl//2
            while heap[par] > heap[chl]:
                heap[par], heap[chl] = heap[chl], heap[par]
                chl = par
                par = chl//2
    a = N
    max_v = 0
    while a > 1:
        max_v += heap[a//2]
        a //= 2
    print(f'#{tc} {max_v}')