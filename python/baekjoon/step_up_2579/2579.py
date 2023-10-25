import sys
sys.stdin = open('input.txt', 'r')


N = int(input())
arr = [int(input()) for _ in range(N)]
dp = [0]*N
p = -1
while True:
    p+=3
    tmp1 = arr[p-2]+arr[p-1]
    tmp2 = arr[p-2]+arr[p]