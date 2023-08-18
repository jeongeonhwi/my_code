import sys
sys.stdin = open('input.txt')


K = int(input())
double = []
arr = []
for _ in range(6):
    a, b = map(int, input().split())
    if a in arr:
        double.append(a)
        double.append(b)
    else:
        arr.append(a)
        arr.append(b)
small = []
for i in range(len(double)//2):
    for j in range(len(arr)//2):
        if double[i*2] == arr[j*2]:
            if double[i*2+1] > arr[j*2+1]:
                small.append(arr[j*2])
                small.append(arr[j*2+1])
            else:
                small.append(double[i*2])
                small.append(double[i*2+1])
arr2 = double + arr
max_v = 0
max_idx = 0
for i in range(len(small)//2):
    for j in range(len(arr2)//2):
        if small[i*2] == arr2[j*2]:
            arr2[j*2] = 0
            arr2[j*2+1] = 0
print(arr2)