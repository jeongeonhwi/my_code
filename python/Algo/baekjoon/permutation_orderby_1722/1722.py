import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

from itertools import permutations

N = int(input())
arr = list(map(int, input().split()))
a = arr[1:]

number = [i for i in range(1, N+1)]

for i, v in enumerate(permutations(number)):
    if arr[0] == 1:
        if i == arr[1]-1:
            print(*v)
            break
    else:
        if list(v) == a:
            print(i+1)
            break