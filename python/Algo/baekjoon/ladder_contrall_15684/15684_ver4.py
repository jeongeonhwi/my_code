import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline



from itertools import combinations
N, M, H = map(int, input().split())
arr = [[0]*(N+N) for _ in range(2*H+1)]
abset = set()
for i in range(2*H+1):
    for j in range(2*N):
        if j%2==1:
            arr[i][j] = 1
for _ in range(M):
    a,b = map(int, input().split())
    arr[2*(a)-1][2*b] = 1
    abset.add((2*(a)-1,2*b))
num = set()
for i in range(2*H):
    for j in range(2*N):
        if j != 0 and i%2==1 and j%2==0:
            if arr[i][j-2] != 1 and arr[i][j] != 1:
                if j+2>=2*N or arr[i][j+2] != 1:
                    num.add((i,j))
ans = -1
pcheck = False
for m in range(4):
    if m != 0:
        combi = combinations(num,m)
        for com in combi:
            check = 0
            for p in com:
                double = set(com)|abset
                if (p[0], p[1] + 2) in double or (p[0], p[1] - 2) in double:
                    pcheck = True
                    break
            if pcheck:
                pcheck = False
                continue
            for p in com:
                arr[p[0]][p[1]] = 1
            jcheck = False
            for j in range(2 * N):
                visited = [[0] * (N + N) for _ in range(2 * H + 1)]
                if arr[0][j] == 1:
                    ni, nj = 0, j
                    visited[ni][nj] = 1
                    while True:
                        if ni >= 2 * H:
                            if nj == j:
                                check += 1
                            else:
                                jcheck = True
                            break
                        for di, dj in [(0, -1), (0, 1), (1, 0)]:
                            tmpi, tmpj = ni + di, nj + dj
                            if 0 <= tmpi < (2 * H + 1) and 0 <= tmpj < (2 * N):
                                if arr[tmpi][tmpj] == 1 and visited[tmpi][tmpj] == 0:
                                    visited[tmpi][tmpj] = 1
                                    ni, nj = tmpi, tmpj
                                    break
                    if jcheck:
                        break
                    if check == N:
                        break
            if check == N:
                ans = m
                break
            for p in com:
                arr[p[0]][p[1]] = 0
        if ans != -1:
            break
    else:
        check = 0
        jcheck = False
        for j in range(2 * N):
            if jcheck:
                break
            visited = [[0] * (N + N) for _ in range(2 * H + 1)]
            if arr[0][j] == 1:
                ni, nj = 0, j
                visited[ni][nj] = 1
                while True:
                    if ni >= 2 * H:
                        if nj == j:
                            check += 1
                        else:
                            jcheck = True
                        break
                    for di, dj in [(0, -1), (0, 1), (1, 0)]:
                        tmpi, tmpj = ni + di, nj + dj
                        if 0 <= tmpi < (2 * H + 1) and 0 <= tmpj < (2 * N):
                            if arr[tmpi][tmpj] == 1 and visited[tmpi][tmpj] == 0:
                                visited[tmpi][tmpj] = 1
                                ni, nj = tmpi, tmpj
                                break
            if jcheck:
                break
            if check == N:
                break
        if check == N:
            ans = m
            break
    if ans != -1:
        break
print(ans)

