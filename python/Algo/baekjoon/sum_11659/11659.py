import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N,M = map(int, input().split())
arr = list(map(int, input().split()))
sum_arr = []
sum_i = 0
for i in arr:
    sum_i += i
    sum_arr.append(sum_i)
for _ in range(M):
    s,e = map(int, input().split())
    if s != 1:
        print(sum_arr[e-1]-sum_arr[s-2])
    else:
        print(sum_arr[e-1])
