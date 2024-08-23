import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline


N = int(input())
arr = list(map(int, input().split()))
arr.sort()
sim_v = 4000000000
ans = []
for ni in range(N-2):
    left,right = ni+1, N-1
    while left < right:
        sum_liquid = arr[ni] + arr[left] + arr[right]
        if abs(sum_liquid) < sim_v:
            sim_v = abs(sum_liquid)
            ans = [arr[ni], arr[left], arr[right]]
        if sum_liquid < 0:
            left += 1
        elif sum_liquid > 0:
            right -= 1
        else:
            break

print(*ans)