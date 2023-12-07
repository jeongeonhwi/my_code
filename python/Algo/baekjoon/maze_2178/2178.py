import sys
sys.stdin = open('input.txt')

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]


N, M = list(map(int, input().split()))
arr = [list(input()) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
stri = 0
strj = 0
total = 1
stack = []
visited[stri][strj] = 1
while True:
    if stri == N and strj == M:
        break
    for k in range(4):
        ni = stri+di[k]
        nj = strj+dj[k]
        if 0<=ni<N and 0<=nj<M:
            if arr[ni][nj] == '1' and visited[ni][nj] == 0:
