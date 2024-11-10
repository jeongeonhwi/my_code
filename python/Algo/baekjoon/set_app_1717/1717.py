import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def union(x,y):
    x = find_set(x)
    y = find_set(y)
    if x == y:
        return
    if x < y:
        node[y] = x
    else:
        node[x] = y


def find_set(x):
    if node[x] == x:
        return x
    node[x] = find_set(node[x])
    return node[x]


n,m = map(int, input().split())
node = [i for i in range(n+1)]
for _ in range(m):
    o,a,b = map(int, input().split())
    if o == 1:
        if find_set(a) == find_set(b):
            print('yes')
        else:
            print('no')
    else:
        union(a,b)