import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

from collections import deque


def fire():
    tmpset = set()
    tmpdelete = set()
    for i,j in fire_position:
        check = 0
        for ni,nj in [(i+1,j),(i,j+1),(i-1,j),(i,j-1)]:
            if 0<=ni<h and 0<=nj<w and fire_visited[ni][nj] == 0 and arr[ni][nj] == '.':
                arr[ni][nj] = '*'
                fire_visited[ni][nj] = 1
                tmpset.add((ni,nj))
                check += 1
        if check == 0:
            tmpdelete.add((i,j))
    fire_position.update(tmpset)
    tmp = fire_position - tmpdelete
    fire_position.clear()
    fire_position.update(tmp)


def dfs(si,sj):
    visited = [[0] * w for _ in range(h)]
    visited[si][sj] = 1
    q = deque([(si,sj,0)])
    level = 0
    while q:
        i,j,cnt = q.popleft()
        if level < cnt + 1:
            level += 1
            fire()
        for ni,nj in [(i+1,j),(i,j+1),(i-1,j),(i,j-1)]:
            if 0<=ni<h and 0<=nj<w:
                if visited[ni][nj] == 0 and arr[ni][nj] == '.':
                    visited[ni][nj] = 1
                    q.append((ni,nj,cnt+1))
            else:
                return cnt+1
    return 'IMPOSSIBLE'




T = int(input())
for _ in range(T):
    w,h = map(int, input().split())
    arr = [list(input().strip()) for _ in range(h)]
    fire_position = set()
    fire_visited = [[0]*w for _ in range(h)]
    si,sj = 0, 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] == '*':
                fire_position.add((i,j))
                fire_visited[i][j] = 1
            elif arr[i][j] == '@':
                si,sj = i, j
                arr[i][j] = '.'
    print(dfs(si,sj))
