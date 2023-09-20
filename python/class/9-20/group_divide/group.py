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



T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    number = [i for i in range(N+1)]
    for m in range(M):
        union(arr[m*2], arr[m*2+1])
    # print(number)
    my_set = set()
    my_list = []
    print(number)
    for i in range(1, N+1):
        my_list.append(find_set(i))
    my_list = set(my_list)
    print(f'#{tc} {len(my_list)}')
