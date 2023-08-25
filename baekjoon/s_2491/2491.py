import sys
sys.stdin = open('input.txt', 'r')


N = int(input())
arr = list(map(int, input().split()))
total = 1
count = 1
count2 = 1
for i in range(N-1):
    if arr[i] <= arr[i+1]:
        count += 1
        if total < count:
            total = count
    else:
        count = 1
for i in range(N-1, 0, -1):
    if arr[i] <= arr[i-1]:
        count2 += 1
        if total < count2:
            total = count2
    else:
        count2 = 1
print(total)