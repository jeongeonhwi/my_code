import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
arr = [[] for _ in range(200003)]
min_v = 300000
max_v = -1
for _ in range(N):
    x,y = map(int, input().split())
    arr[y+100000].append(x)
    min_v = min(y+100000, min_v)
    max_v = max(y+100000, max_v)
for i in range(min_v, max_v+1):
    if arr[i]:
        if len(arr[i]) == 1:
            print(f'{arr[i][0]} {i-100000}')
        else:
            arr[i].sort()
            for ii in arr[i]:
                print(f'{ii} {i - 100000}')