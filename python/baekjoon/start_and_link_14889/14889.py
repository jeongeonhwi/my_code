import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


def permutation(start, end):
    if start == end:
        c = tuple(p)
        my_set.add(c)
        return
    for j in range(N):
        if used[j] == 0:
            p[start] = num[j]
            used[j] = 1
            permutation(start+1, end)
            used[j] = 0


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
num = [i for i in range(N)]
used = [0]*N
p = [0]*N
my_set = set()
permutation(0,N)
min_v = 10000
for m in my_set:
    start = 0
    link = 0
    for i in range(N//2):
        for j in range(N//2):
            start += arr[m[i]][m[j]]
            link += arr[m[N//2+i]][m[N//2+j]]
    min_v = min(min_v, abs(start-link))
print(min_v)