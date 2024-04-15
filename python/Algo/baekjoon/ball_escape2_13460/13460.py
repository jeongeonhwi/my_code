import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

from collections import deque

def find_thing():
    red, blue, whole = 0,0,0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                red = (i,j)
                board[i][j] = '.'
            elif board[i][j] == 'O':
                whole = (i,j)
            elif board[i][j] == 'B':
                blue = (i,j)
                board[i][j] = '.'
    return red, blue, whole


def dfs(start, problem):
    q = deque([(start[0], start[1], problem[0], problem[1], 0)])

    while q:
        i, j, pi, pj, cnt = q.popleft()

        if cnt > 9:
            continue

        for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1),]:
            ni,nj = i+di, j+dj
            tmp_pi, tmp_pj = pi,pj
            nextcnt = cnt+1
            blue_flag = False
            whole_flag = False
            while True:
                if board[ni][nj] == 'O':
                    if blue_flag:
                        whole_flag = True
                        break
                    else:
                        while True:
                            if board[tmp_pi][tmp_pj] == '#':
                                break
                            if board[tmp_pi][tmp_pj] == 'O':
                                whole_flag = True
                                break
                            tmp_pi, tmp_pj = tmp_pi + di, tmp_pj + dj
                        if whole_flag:
                            break
                        return nextcnt
                if board[ni][nj] == '#':
                    ni,nj = ni-di, nj-dj
                    break
                if ni == pi and nj == pj:
                    blue_flag = True
                ni,nj = ni+di, nj+dj
            if blue_flag:
                tmp_pi, tmp_pj = ni, nj
                ni, nj = ni-di, nj-dj
            else:
                while True:
                    if board[tmp_pi][tmp_pj] == 'O':
                        whole_flag = True
                        break
                    if board[tmp_pi][tmp_pj] == '#':
                        tmp_pi, tmp_pj = tmp_pi - di, tmp_pj - dj
                        break
                    if tmp_pi == ni and tmp_pj == nj:
                        tmp_pi, tmp_pj = tmp_pi - di, tmp_pj - dj
                        break
                    tmp_pi, tmp_pj = tmp_pi + di, tmp_pj + dj

            if whole_flag == False:
                if visited[ni][nj][tmp_pi][tmp_pj] == 0:
                    visited[ni][nj][tmp_pi][tmp_pj] = 1
                    q.append((ni,nj,tmp_pi,tmp_pj,nextcnt))
    return -1


n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]
visited = [[[[0 for _ in range(m)] for _ in range(n)] for _ in range(m)] for _ in range(n)]

red, blue, whole = find_thing()

ans = dfs(red, blue)

print(ans)