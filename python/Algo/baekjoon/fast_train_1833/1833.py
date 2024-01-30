import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

# 음수는 이미 설치된 고석철도
# 10000을 넘지 않는 지연수는 설치 비용



def find_set(x):
    if parent[x] == x:
        return x
    parent[x] = find_set(parent[x])
    return parent[x]

def union(x,y):
    pass

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
cost = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] < 0:
            cost -= arr[i][j]
            arr[i][j] = 0
            union(i,j)
        elif arr[i][j] > 0:
            my.append((arr[i][j], i, j))
cost //= 2

print(daic(0))