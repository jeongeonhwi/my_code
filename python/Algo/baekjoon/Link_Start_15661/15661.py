import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

num = [i for i in range(N)]
ans = float('inf')
min_link = float('inf')
for i in range(1, 1<<N):
    start = set()
    for j in range(N):
        if i&(1<<j):
            start.add(num[j])
    if len(start) == N:
        continue
    link = set(num) - start
    link_cnt = 0
    start_cnt = 0
    for i in link:
        for j in link:
            link_cnt += arr[i][j]
    for i in start:
        for j in start:
            start_cnt += arr[i][j]
    min_link = min(min_link,link_cnt)
    ans = min(ans, abs(start_cnt-link_cnt))
print(ans)