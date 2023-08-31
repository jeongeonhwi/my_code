import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    A, N = map(int, input().split())
    arr = list(str(A))
    arr1 = []
    for i in arr:
        arr1.append(int(i))
    arr = arr1[:]
    arr1.sort(reverse=True)
    idx = 0
    a = ''.join(map(str, arr))
    b = ''.join(map(str, arr1))
    if int(b) > int(a):
        for i in range(len(arr1)):
            if arr1[i] != arr[i]:
                max_idx = 0
                max_v = 0
                check = False
                for j in range(len(arr)-1, i, -1):
                    if arr[j] > max_v:
                        max_v = arr[j]
                        max_idx = j
                        check = True
                count1 = arr.count(max(arr[i:]))
                if arr[i] != arr[max_idx] and check == True:
                    arr[i], arr[max_idx] = arr[max_idx], arr[i]
                    N -= 1
                if N <=0:
                    break
                if int(b) == int(a):
                    break
    # print(arr)
    check = False
    while N >0:
        if arr1 == arr:
            for i in arr:
                if arr.count(i) >= 2:
                    check = True
                    break
        if check:
            break
        arr[-2], arr[-1] = arr[-1], arr[-2]
        N -= 1
    print(f'#{tc} ', end='')
    for i in arr:
        print(i, end='')
    print()