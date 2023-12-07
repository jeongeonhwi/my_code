import sys
sys.stdin = open('input.txt')

import sys
N, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
current_tem = 0
for i in range(K):
    current_tem += arr[i]
max_tem = current_tem
if K > 1:
    for i in range(K, N):
        if current_tem + arr[i] - arr[i-K] > max_tem:
            max_tem = current_tem + arr[i] - arr[i-K]
        current_tem += arr[i] - arr[i-K]
elif K == 1:
    arr.sort(reverse=True)
    max_tem = arr[0]
print(max_tem)