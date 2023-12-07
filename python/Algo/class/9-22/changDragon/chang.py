import sys
sys.stdin = open('input.txt', 'r')


def find_set(x):
    if number[x] == x:
        return x
    number[x] = find_set(number[x])
    return number[x]

def union(x, y):
    x = find_set(x)
    y = find_set(y)
    if x == y:
        return
    if x < y:
        number[y] = x
    else:
        number[x] = y






T =  int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    number = [i for i in range(N)]
    arr = [[] for _ in range(N)]
    for _ in range(M):
        s, e = map(int, input().split())
        arr[s-1].append(e-1)
        arr[e-1].append(s-1)
    for i in range(len(arr)):
        for j in arr[i]:
            union(i,j)
    my_set = set()
    for i in range(N):
        my_set.add(find_set(i))
    print(f'#{tc} {len(my_set)}')