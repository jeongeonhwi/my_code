import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

# 음수는 이미 설치된 고석철도
# 10000을 넘지 않는 지연수는 설치 비용


def find_set(x):
    if parents[x] == x:
        return x
    parents[x] = find_set(parents[x])
    return parents[x]

def union(x,y):
    x = find_set(x)
    y = find_set(y)
    if x == y:
        return
    if x < y:
        parents[y] = x
    else:
        parents[x] = y


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
parents = [i for i in range(N)]
my = []
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
my.sort()
cnt = 0
check = set()
node_position = []
for i in range(N):
    check.add(find_set(i))
if len(check) == 1:
    print(cost, cnt)
else:
    check.clear()
    for c, i, j in my:
        if find_set(i) != find_set(j):
            cnt += 1
            cost += c
            node_position.append((i,j))
            union(i,j)
            for i in range(N):
                check.add(find_set(i))
            if len(check) == 1:
                print(cost, cnt)
                for i in node_position:
                    print(i[0]+1, i[1]+1)
                break
            else:
                check.clear()