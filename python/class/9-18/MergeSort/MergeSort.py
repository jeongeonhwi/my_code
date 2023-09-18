import sys
sys.stdin  = open('input.txt', 'r')




def merge_sort(arr):
    if len(arr) == 1:
        return arr
    left = merge_sort(arr[:len(arr)//2])
    right = merge_sort(arr[len(arr)//2:])
    return merge(left, right)


def merge(left, right):
    global cnt
    result = left+right
    if left[-1] > right[-1]:
        cnt+=1
    idx = 0
    lidx = 0
    ridx = 0
    while len(left)>lidx and len(right)>ridx:
        if left[lidx] < right[ridx]:
            result[idx] = left[lidx]
            idx += 1
            lidx += 1
        elif left[lidx] > right[ridx]:
            result[idx] = right[ridx]
            idx += 1
            ridx += 1
        else:
            result[idx] = left[lidx]
            idx+= 1
            lidx+=1
            result[idx] = right[ridx]
            idx+=1
            ridx+=1
    if len(left) > lidx:
        while len(left) > lidx:
            result[idx] = left[lidx]
            idx+= 1
            lidx+=1
    else:
        while len(right) > ridx:
            result[idx] = right[ridx]
            idx += 1
            ridx += 1
    return result



T = int(input())
for tc in range(1, T+1):
    cnt = 0
    N = int(input())
    arr = list(map(int, input().split()))
    n = merge_sort(arr)
    print(f'#{tc} {n[N // 2]} {cnt}')

