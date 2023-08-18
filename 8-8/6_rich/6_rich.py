import sys
sys.stdin = open('input.txt')

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    idx = 0
    result = 0
    while idx < len(arr):
        maxlist = quick_sort(arr[idx:])
        for i in range(len(arr)):
            if arr[i] == maxlist[len(maxlist)-1]:
                count = i
        # print(idx)
        sum = 0
        arrx = arr[idx:]
        # print(arrx)
        for i in range(len(arrx)):
            if i+idx < count:
                sum += arrx[i]
            if i+idx == count:
                result += arrx[i]*(i-1+1) - sum
                break
        idx = count + 1

    print(f'#{tc} {result}')