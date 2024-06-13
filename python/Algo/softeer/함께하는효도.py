import sys

input = sys.stdin.readline
from itertools import permutations


def dfs(si, sj, friend_i):
    global tmp_v
    stack = [(si, sj, arr[si][sj], 0, [(si, sj)])]
    while stack:
        i, j, cnt, step, visi = stack.pop()
        if step >= 3:
            visited[friend_i].append(visi)
            continue
        for ni, nj in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1), ]:
            if 0 <= ni < n and 0 <= nj < n:
                nextcnt = cnt + arr[ni][nj]
                nextstep = step + 1
                stack.append((ni, nj, nextcnt, nextstep, visi + [(ni, nj)]))


def func(depth, m, save_tmp):
    global max_v
    if depth == m:
        tmp_v = 0
        tmp_set = set()
        for sa in save_tmp:
            for s in sa:
                tmp_set.add(s)
        for ti, tj in tmp_set:
            tmp_v += arr[ti][tj]
        max_v = max(tmp_v, max_v)
        return

    for x in visited[depth]:
        save_tmp.append(x)
        func(depth + 1, m, save_tmp)
        save_tmp.pop()


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
friend_position = [list(map(int, input().split())) for _ in range(m)]
visited = [[] for _ in range(3)]
max_v = 0
for i in range(len(friend_position)):
    dfs(friend_position[i][0] - 1, friend_position[i][1] - 1, i)

func(0, m, [])
print(max_v)