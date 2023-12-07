import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline





di = [1,-1,0,0,1,-1,1,-1]
dj = [0,0,1,-1,1,1,-1,-1]
ddi = [0,1,0,-1]
ddj = [1,0,-1,0]
N = int(input())
arr = [list(input()) for _ in range(N)]
si,sj = 1,1
k = 0
if N >= 3:
    while True:
        if k != 0 and si == 1 and sj == 1:
            break
        check = True
        for kk in range(8):
            ni,nj = si+di[kk], sj+dj[kk]
            if arr[ni][nj] == '0':
                check = False
        if check:
            for kk in range(8):
                ni,nj = si+di[kk], sj+dj[kk]
                if arr[ni][nj] == '0':
                    continue
                if arr[ni][nj] == '1':
                    arr[ni][nj] = '0'
                    arr[si][sj] = '*'
                elif arr[ni][nj] == '2':
                    arr[ni][nj] = '1'
                    arr[si][sj] = '*'
                elif arr[ni][nj] == '3':
                    arr[ni][nj] = '2'
                    arr[si][sj] = '*'
        si,sj = si+ddi[k], sj+ddj[k]
        if 1<=si<N-1 and 1<=sj<N-1:
            continue
        else:
            si,sj = si-ddi[k], sj-ddj[k]
            k+=1

ans = 0
for i in arr:
    for j in i:
        if j == '*':
            ans += 1
if N > 3:
    print(ans + (N-4)**2)
elif N == 3:
    print(ans)
else:
    print(0)