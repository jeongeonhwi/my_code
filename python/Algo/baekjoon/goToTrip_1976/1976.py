import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

def union(x,y):
    x = parent[x]
    y = parent[y]
    if x == y:
        return
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


def find_set(x):
    if parent[x] == x:
        return x
    parent[x] = find_set(parent[x])
    return parent[x]


N = int(input())
M = int(input())
arr = [[*map(int, input().split())] for _ in range(N)]
trip_root = list(map(int, input().split()))
parent = [i for i in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and find_set(i) != find_set(j):
            union(i,j)
flag = find_set(trip_root[0]-1)
for i in range(M):
    if flag != find_set(trip_root[i]-1):
        print('NO')
        break
else:
    print('YES')