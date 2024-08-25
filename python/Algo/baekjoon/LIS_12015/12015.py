import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
length_list = [0]*N
for k in range(N):
    length_list[k] = 1
    for i in range(k):
        if arr[i] < arr[k]:
            length_list[k] = max(length_list[k], length_list[i]+1)
print(max(length_list))