import sys
sys.stdin = open('input.txt', 'r')


def find_first(arr):
    stack = []
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0:
                stack.append((i,j))
                arr[i][j] = 0
                return stack


def find_top(arr):
    stack = find_first(arr)
    while stack:
        i, j = stack.pop()
        for k in range(4):
            ni = i+di[k]
            nj = j+dj[k]
            if arr[ni][nj] != 0:





di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
