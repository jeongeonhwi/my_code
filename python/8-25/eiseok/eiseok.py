import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    arr = [list(input()) for _ in range(5)]
    print(f'#{tc} ', end='')
    max_len = 0
    for k in range(5):
        if max_len <= len(arr[k]):
            max_len = len(arr[k])
    # print(max_len)
    for k in range(5):
        if len(arr[k]) < max_len:
            for _ in range(max_len-len(arr[k])):
                arr[k].append('')
            # print(arr[k])
    for j in range(max_len):
        for i in range(5):
            print(arr[i][j], end='')
    print()