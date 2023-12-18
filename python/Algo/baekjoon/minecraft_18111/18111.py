import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

runtime, max_h = float('inf'),0
for g in range(min(map(min, arr)), max(map(max, arr))+1):
    tr, tb = 0,B
    for i in range(N):
        for j in range(M):
            if arr[i][j] > g:
                tr += (arr[i][j] - g)*2
                tb += (arr[i][j] - g)
            else:
                tr += (g - arr[i][j])
                tb -= (g - arr[i][j])
    if tb < 0:
        continue
    if runtime >= tr:
        runtime, max_h = tr, max(max_h, g)
print(f'{runtime} {max_h}')