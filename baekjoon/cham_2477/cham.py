import sys
sys.stdin = open('input.txt')


K = int(input())
num = []
arr = []
for _ in range(6):
    a, b = map(int, input().split())
    num.append(a)
    arr.append(b)
min_idx = 0
for i in range(len(num)):
    if num[i%6] == num[(i+2)%6] and num[(i+1)%6] == num[(i+3)%6]:
        min_idx = i
        break
min_v = arr[(min_idx+1)%6]*arr[(min_idx+2)%6]
max_v = arr[(min_idx+4)%6]*arr[(min_idx+5)%6]


print((max_v-min_v)*K)