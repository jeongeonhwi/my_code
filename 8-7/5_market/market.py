import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    total = 0
    stotal = 0
    result = 0
    for i in range(N-1):
        total += 1
        stotal += arr[i]
        if arr[i+1]*total - stotal > result:
            result = arr[i+1]*total - stotal
    print(f'#{tc} {result}')