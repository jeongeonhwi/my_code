import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
arr = []
for _ in range(N*2):
    a = list(map(int, input().split()))
    b = a[1:]
    arr.append(b)
print(arr)
for i in range(N):
    if arr[i*2].count(4) > arr[i*2+1].count(4):
        print('A')
    elif arr[i*2].count(4) < arr[i*2+1].count(4):
        print('B')
    elif arr[i*2].count(3) > arr[i*2+1].count(3):
        print('A')
    elif arr[i*2].count(3) < arr[i*2+1].count(3):
        print('B')
    elif arr[i*2].count(2) > arr[i*2+1].count(2):
        print('A')
    elif arr[i*2].count(2) < arr[i*2+1].count(2):
        print('B')
    elif arr[i*2].count(1) > arr[i*2+1].count(1):
        print('A')
    elif arr[i*2].count(1) < arr[i*2+1].count(1):
        print('B')
    else:
        print('D')