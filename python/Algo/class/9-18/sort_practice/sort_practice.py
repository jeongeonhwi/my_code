import sys
sys.stdin = open('input.txt', 'r')


def quick(arr):
    if len(arr)<=1:
        return arr
    pivot = arr[len(arr)//2]
    left, equal, right = [], [], []
    for i in arr:
        if pivot > i:
            left.append(i)
        elif pivot < i:
            right.append(i)
        else:
            equal.append(i)
    return quick(left) + equal + quick(right)



T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    ans = quick(arr)
    print(f'#{tc}', end=' ')
    print(*ans)