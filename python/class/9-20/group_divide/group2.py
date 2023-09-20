import sys
sys.stdin = open('input.txt', 'r')

# 실패한 코드 왜 number를 직접 접속하면 틀릴까??

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


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    number = [i for i in range(N)]
    for m in range(M):
        union(arr[m * 2] - 1, arr[m * 2 + 1] - 1)
    my_set = set()
    for i in number:
        my_set.add(number[i])
    print(f'#{tc} {len(my_set)}')