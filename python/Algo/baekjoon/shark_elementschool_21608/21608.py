import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
data = []
for _ in range(N**2):
    a, b, c, d, e = map(int, input().split())
    data.append((a, {b,c,d,e}))
arr = [[0]*N for _ in range(N)]
arr[1][1] = data[0][0]
ans_list = [(1,1,data[0][1])]
for d in range(1, N**2):
    check = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                cnt = 0
                blank = 0
                for n in [(1,0), (0,1), (-1,0), (0,-1)]:
                    ni,nj = i+n[0], j+n[1]
                    if 0<=ni<N and 0<=nj<N:
                        if arr[ni][nj] in data[d][1]:
                            cnt += 1
                        if arr[ni][nj] == 0:
                            blank += 1
                check.append((cnt,blank,i,j))
    check.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
    arr[check[0][2]][check[0][3]] = data[d][0]
    ans_list.append((check[0][2], check[0][3], data[d][1]))
ans = 0
for a in ans_list:
    cnt = 0
    for n in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        ni, nj = a[0] + n[0], a[1] + n[1]
        if 0 <= ni < N and 0 <= nj < N:
            if arr[ni][nj] in a[2]:
                cnt += 1
    if cnt == 1:
        ans += 1
    elif cnt == 2:
        ans += 10
    elif cnt == 3:
        ans += 100
    elif cnt == 4:
        ans += 1000

print(ans)