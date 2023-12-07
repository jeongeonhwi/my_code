import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline


def find_chicken(arr):
    chicken = set()
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                chicken.add((i,j))
    return chicken

def find_home(arr):
    home = set()
    for i in range(N):
        for j in range(N):
            if arr[i][j]== 1:
                home.add((i,j))
    return home

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
chicken = find_chicken(arr)
home = find_home(arr)
chicken = list(chicken)
min_v = 10000000
for i in range(1<<len(chicken)):
    group = set()
    for j in range(len(chicken)):
        if i&(1<<j):
            group.add(chicken[j])
    if len(group) != M:
        continue
    cnt = 0
    for hi,hj in home:
        tmp = set()
        for ci,cj in group:
            tmp.add(abs(hi-ci)+abs(hj-cj))
        cnt+=min(tmp)
    min_v = min(min_v,cnt)
print(min_v)
