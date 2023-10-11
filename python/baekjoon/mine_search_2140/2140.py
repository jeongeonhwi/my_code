import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline





di = [1,-1,0,0,1,-1,1,-1]
dj = [0,0,1,-1,1,1,-1,-1]
N = int(input())
arr = [list(input()) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j] == '0' or arr[i][j] == '#' or arr[i][j] == '*':
            continue
        mine = 0
        shyap = 0
        for k in range(8):
            ni,nj = i+di[k], j+dj[k]
            if 0<=ni<N and 0<=nj<N:
                if arr[ni][nj] == '#':
                    shyap += 1
                elif arr[ni][nj] == '*':
                    mine += 1
        if shyap == int(arr[i][j])-mine:
            for k in range(8):
                ni, nj = i+ di[k], j + dj[k]
                if 0 <= ni < N and 0 <= nj < N:
                    if arr[ni][nj] != '#':
                        continue
                    arr[ni][nj] = '*'
for i in range(N):
    for j in range(N):
        if arr[i][j] == '0' or arr[i][j] == '#' or arr[i][j] == '*':
            continue
        mine = 0
        one = False
        oi, oj = 0,0
        two = False
        for k in range(8):
            ni,nj = i+di[k], j+dj[k]
            if 0<=ni<N and 0<=nj<N:
                if arr[ni][nj] == '*':
                    mine += 1
                if arr[ni][nj] == '1':
                    one = True
                    oi,oj = ni,nj
                if arr[ni][nj] == '2':
                    two = True
        if mine == int(arr[i][j]):
            continue
        one = False
        oi, oj = 0, 0
        two = False
        for k in range(8):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] == '1':
                    one = True
                    oi, oj = ni, nj
                if arr[ni][nj] == '2':
                    two = True
        if one:
            if arr[i][j] == '1':
                if i == 0:
                    if arr[oi + 1][oj] != '#':
                        continue
                    arr[oi + 1][oj] = '*'
                else:
                    if arr[oi - 1][oj] != '#':
                        continue
                    arr[oi - 1][oj] = '*'
                if j == 0:
                    if arr[oi][oj + 1] != '#':
                        continue
                    arr[oi][oj + 1] = '*'
                else:
                    if arr[oi][oj - 1] != '#':
                        continue
                    arr[oi][oj - 1] = '*'

ans = 0
for i in arr:
    for j in i:
        if j == '*':
            ans += 1
for i in arr:
    print(i)
print(ans + (N-4)**2)