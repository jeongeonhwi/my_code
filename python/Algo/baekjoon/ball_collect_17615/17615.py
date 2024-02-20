import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

# 양끝점에 가장 많이 모여있는 무더기 찾기
def find_ball(arr):
    cnt = 0
    lcheck = True
    left = arr[0]
    lc = 0
    rcheck = True
    right = arr[-1]
    rc = 0
    for i in range(len(arr)):
        if lcheck and left == arr[i]:
            lc += 1
        else:
            lcheck = False
        if rcheck and right == arr[len(arr)-1-i]:
            rc += 1
        else:
            rcheck = False
    return min(arr.count(left) - lc, arr.count(right) - rc)
N = int(input())
arr = list(input().strip())
print(find_ball(arr))