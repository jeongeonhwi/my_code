import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T + 1):
    N = int(input())
    arr = [0] * (N + 1)
    for _ in range(N):
        alist = list(input().split())
        if len(alist) == 4:
            arr[int(alist[0])] = alist[1:]
        else:
            arr[int(alist[0])] = int(alist[1])
    # s_idx = 0
    # for i in arr:
    #     if type(i) == list:
    #         s_idx += 1
    print(arr)
    for i in range(len(arr)-1, -1, -1):
        if type(arr[i]) == list:
            if arr[i][0] == '-':
                a = arr[int(arr[i][1])] - arr[int(arr[i][2])]
                arr[i] = a
            elif arr[i][0] == '+':
                a = arr[int(arr[i][1])] + arr[int(arr[i][2])]
                arr[i] = a
            elif arr[i][0] == '/':
                a = arr[int(arr[i][1])] / arr[int(arr[i][2])]
                arr[i] = a
            elif arr[i][0] == '*':
                a = arr[int(arr[i][1])] * arr[int(arr[i][2])]
                arr[i] = a

    print(f'#{tc} {int(arr[1])}')


