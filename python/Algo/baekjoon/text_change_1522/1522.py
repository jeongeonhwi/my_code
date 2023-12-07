import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')




N = list(input())
b = N.count('b')
n = len(N)
a = N.count('a')
min_v = float('inf')
N = N+N[:a-1]
for i in range(n):
    c = 0
    for j in range(a):
        if N[(i+j)] == 'b':
            c+=1
    min_v = min(min_v,c)
print(min_v)