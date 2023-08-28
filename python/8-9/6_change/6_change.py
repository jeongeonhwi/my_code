import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    A, N = map(int, input().split())
    arr = list(str(A))
    # max_v = arr[-1]
    # maxidx = 0
    # min_v = arr[-1]
    # minidx = 0
    # for i in range(N):
    #     if i <= len(arr):
    #         for j in range(len(arr)-i):
    #             if arr[j+i] >= max_v:
    #                 max_v = arr[j+i]
    #                 maxidx = j+i
    #         if i == maxidx:
    #             max_v = arr[-1]
    #             for j in range(len(arr) - i-1):
    #                 if arr[j + i+1] >= max_v:
    #                     max_v = arr[j + i+1]
    #                     if j + i + 1 > len(arr)-1:
    #                         maxidx = len(arr) -1 -(j + i + 1)
    #             if i+1 > len(arr)-1:
    #                 arr[len(arr) -1 - (i + 1)], arr[maxidx] = arr[maxidx], arr[len(arr) -1 - (i + 1)]
    #                 max_v = arr[-1]
    #             else:
    #                 arr[i+1], arr[maxidx] = arr[maxidx], arr[i+1]
    #                 max_v = arr[-1]
    #         else:
    #             if i > len(arr)-1:
    #                 arr[len(arr) -1 - i], arr[maxidx] = arr[maxidx], arr[len(arr) -1 - i]
    #                 max_v = arr[-1]
    #             else:
    #                 arr[i], arr[maxidx] = arr[maxidx], arr[i]
    #                 max_v = arr[-1]
    #
    # print(f'#{tc}', end=' ')
    # for i in range(len(arr)):
    #     print(arr[i], end='')
    # print()




    max_v = arr[-1]
    maxidx = 0
    for i in range(N):
        if i < len(arr):
            for j in range(len(arr) - i):
                if arr[j + i] >= max_v:
                    max_v = arr[j + i]
                    maxidx = j + i
            if i == maxidx:
                max_v = arr[-1]
                for j in range(len(arr) - i - 1):
                    if arr[j + i + 1] >= max_v:
                        max_v = arr[j + i + 1]
                        if j + i + 1 > len(arr) - 1:
                            maxidx = len(arr) - 1 - (j + i + 1)
                if i + 1 <= len(arr) - 1:
                    arr[i + 1], arr[maxidx] = arr[maxidx], arr[i + 1]
                    max_v = arr[-1]
            else:
                arr[i], arr[maxidx] = arr[maxidx], arr[i]
                max_v = arr[-1]
        else:
            if (i-len(arr)-1)%2 != 0:
                arr[-1], arr[-2] = arr[-2], arr[-1]

    print(f'#{tc}', end=' ')
    for i in range(len(arr)):
        print(arr[i], end='')
    print()












