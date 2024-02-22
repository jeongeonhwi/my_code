import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

n,l = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(l):
    print(min(arr[:i+1]))
for i in range(l,n):
    print(min(arr[i-l+1:i+1]))