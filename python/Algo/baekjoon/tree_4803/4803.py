import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

def find_set(x):
    if parent[x] == x:
        return x
    parent[x] = find_set(parent[x])
    return parent[x]

def union(x,y):
    x = find_set(x)
    y = find_set(y)
    if x == y:
        return
    if x<y:
        parent[y] = x
    else:
        parent[x] =y


T = 1
while True:
    N,M = map(int, input().split())
    if N == 0 and M == 0:
        break
    parent = [i for i in range(N)]
    tree = 0
    check = 0
    cs = set()
    arr = [[] for _ in range(N)]
    for _ in range(M):
        x,y = map(int, input().split())

        if find_set(x-1) != find_set(y-1):
            union(x-1,y-1)
        else:
            check += 1
            cs.add(find_set(x-1))

    cycle = set(parent)
    tree = len(set(parent))-len(cs)
    print(parent)
    print(cs)
    if tree == 0:
        print(f'Case {T}: No trees.')
    elif tree == 1:
        print(f'Case {T}: There is one tree.')
    else:
        print(f'Case {T}: A forest of {tree} trees.')
    T += 1