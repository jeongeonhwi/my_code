import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

num = [i for i in range(N)]
for i in range(1, 1<<N):
    start = set()
    for j in range(N):
        if i&(1<<j):
            start.add(num[j])
    if len(start) == N:
        continue
    link = set(num) - start
    print(link)