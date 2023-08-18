import sys
sys.stdin= open('input.txt')

T = int(input())
for tc in range(1, T+1):
    arr = list(map(str, input()))
    open1 = '('
    close1 = ')'
    # print(arr)
    count = 0
    ans = 0
    for i in range(len(arr)):
        if arr[i] == open1:
            count += 1
        if arr[i] == close1 and arr[i-1] == open1:
            count -= 1
            ans += count
        elif arr[i] == close1:
            count -= 1
            ans += 1
    print(f'#{tc} {ans}')
