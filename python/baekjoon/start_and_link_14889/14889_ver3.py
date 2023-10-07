import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
num = [i for i in range(N)]
nset = set(num)
min_v = 10000
for i in range(1<<N):
    group1 = set()
    for j in range(N):
        if i&(1<<j):
            group1.add(num[j])
    if len(group1) != N//2:
        continue
    group2 = nset - group1
    start = 0
    link = 0
    for i in group1:
        for j in group1:
            start += arr[i][j]
    for i in group2:
        for j in group2:
            link += arr[i][j]
    min_v = min(min_v, abs(start-link))
print(min_v)