import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
s = 2000000001
liquid_list = []
left, right = 0,N-1
while left < right:
    abs_liquid = abs(arr[left]+arr[right])
    if abs_liquid < s:
        s = abs_liquid
        liquid_list = [arr[left], arr[right]]
    if arr[left]+arr[right] < 0:
        left += 1
    elif arr[left]+arr[right] > 0:
        right -= 1
    else:
        liquid_list = [arr[left], arr[right]]
        break
print(*liquid_list)