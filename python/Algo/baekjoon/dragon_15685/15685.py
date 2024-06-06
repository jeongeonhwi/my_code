import sys
sys.stdin = open('input.txt', 'r')
# sys.stdout = open('input.txt', 'w')



di = [0,1,1]
dj = [1,1,0]
N = int(input())
arr = [[0]*102 for _ in range(102)]
for _ in range(N):
    x, y, d, g = map(int, input().split())
    cnt = 0
    arr[y][x] = 1
    ci = y
    cj = x
    q = [(ci,cj)]
    while True:
        if cnt == 0:
            if d == 0:
                arr[y][x+1] = 1
                cj += 1
                q.append((ci,cj))
            elif d == 1:
                arr[y-1][x] = 1
                ci -= 1
                q.append((ci,cj))
            elif d == 2:
                arr[y][x-1] = 1
                cj -= 1
                q.append((ci,cj))
            elif d == 3:
                arr[y+1][x] = 1
                ci += 1
                q.append((ci,cj))
        else:
            tmpci, tmpcj = 0, 0
            tmpq = q[:]
            while tmpq:
                check = False
                i, j = tmpq.pop()
                if i == y and j == x:
                    check = True
                if ci==i and cj<j:
                    tmpi = i-ci
                    tmpj = j-cj
                    i = ci+tmpj
                    j = cj
                    q.append((i,j))
                    arr[i][j] = 1
                elif ci>i and cj<j:
                    tmpi = i-ci
                    tmpj = j-cj
                    i = ci+tmpj
                    j = cj-tmpi
                    q.append((i,j))
                    arr[i][j] = 1
                elif ci==i and cj>j:
                    tmpi = i-ci
                    tmpj = j-cj
                    i = ci+tmpj
                    j = cj
                    q.append((i,j))
                    arr[i][j] = 1
                elif ci<i and cj>j:
                    tmpi = i-ci
                    tmpj = j-cj
                    i = ci+tmpj
                    j = cj-tmpi
                    q.append((i,j))
                    arr[i][j] = 1
                elif ci<i and cj<j:
                    tmpi = i-ci
                    tmpj = j-cj
                    i = ci+tmpj
                    j = cj-tmpi
                    q.append((i,j))
                    arr[i][j] = 1
                elif ci<i and cj==j:
                    tmpi = i-ci
                    tmpj = j-cj
                    i = ci
                    j = cj-tmpi
                    q.append((i,j))
                    arr[i][j] = 1
                elif ci>i and cj>j:
                    tmpi = i-ci
                    tmpj = j-cj
                    i = ci+tmpj
                    j = cj-tmpi
                    q.append((i,j))
                    arr[i][j] = 1
                elif ci>i and cj==j:
                    tmpi = i-ci
                    tmpj = j-cj
                    i = ci
                    j = cj-tmpi
                    q.append((i,j))
                    arr[i][j] = 1
                if check:
                    tmpci = i
                    tmpcj = j
            ci = tmpci
            cj = tmpcj
        if cnt == g:
            break
        else:
            cnt += 1
ans = 0
for i in range(102):
    for j in range(102):
        if arr[i][j] == 1:
            tmp = 0
            for k in range(3):
                ni = i+di[k]
                nj = j+dj[k]
                if arr[ni][nj] == 1:
                    tmp += 1
            if tmp == 3:
                ans += 1
print(ans)