import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    a = 0
    for _ in range(M):
        a = arr.pop(0)
        arr.append(a)
    print(f'#{tc} {arr[0]}')