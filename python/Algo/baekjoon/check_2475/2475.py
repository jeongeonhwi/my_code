import sys
sys.stdin = open('input.txt', 'r')

arr = list(map(int, input().split()))
check = 0
for i in arr:
    check += i**2
print(check%10)