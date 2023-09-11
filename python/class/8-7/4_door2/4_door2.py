import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    arr = list(input())
    count = 0
    for i in range(len(arr)//2):
        if arr[i] == arr[len(arr)-1-i]:
            count += 1
    result = 0
    if count == (len(arr)//2):
        result = 1
    print(f'#{tc} {result}')