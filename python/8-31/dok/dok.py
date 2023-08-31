import sys
sys.stdin = open('input.txt', 'r')

def f(i):
    if i == N:
        return
    for i in arr:



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr.sort(key=lambda x:x[1])
    f(0)