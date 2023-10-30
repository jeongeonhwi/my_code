import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline


T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    tmp = []
    ans = 0
    while True:
        for i in range(len(arr)//2):
            if len(arr) == 1:
                ans += arr[0]
                arr = 0
                break
            sum_tmp = arr[i*2]+arr[i*2+1]
            ans += sum_tmp
            tmp.append(sum_tmp)
        else:
            print(arr)
            if (len(arr)//2)*2 != len(arr):
                if len(arr) == 1:
                    arr = 0
                    break
                tmp.append(arr[len(arr)-1])
            tmp.sort()
            arr = tmp[:]
            tmp.clear()
        if arr == 0:
            break

    print(ans)