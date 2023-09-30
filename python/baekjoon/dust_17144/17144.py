import sys
sys.stdin = open('input.txt', 'r')


import copy
def find_machine(arr):
    i = 0
    while True:
        if arr[i][0] == -1:
            return i
        i+=1

# 위, 오른쪽, 아래, 왼쪽
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
# 아래, 오른쪽, 위 , 왼쪽
ddi = [1, 0, -1, 0]
ddj = [0, 1, 0, -1]
R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
start = find_machine(arr)
for _ in range(T):
    arr2 =[[0]*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if arr[i][j] != -1:
                for k in range(4):
                    ni, nj = i+di[k], j+dj[k]
                    if 0<=ni<R and 0<=nj<C and arr[ni][nj] != -1:
                        arr2[ni][nj] += arr[i][j]//5
                        arr2[i][j] -= arr[i][j]//5
                arr2[i][j] += arr[i][j]
            else:
                arr2[i][j] = arr[i][j]
    arr = copy.deepcopy(arr2)
    upi, upj = start, 0
    ni, nj = upi, upj
    for k in range(4):
        ni += di[k]
        nj += dj[k]
        while True:
            if 0<=ni<=start and 0<=nj<C:
                if arr[ni - di[k]][nj - dj[k]] != -1:
                    arr[ni - di[k]][nj - dj[k]] = arr[ni][nj]
                arr[ni][nj] = 0
                ni += di[k]
                nj += dj[k]
            else:
                ni -= di[k]
                nj -= dj[k]
                break
    upi, upj = start+1, 0
    ni, nj = upi, upj
    for k in range(4):
        ni += ddi[k]
        nj += ddj[k]
        while True:
            if upi<=ni<R and 0<=nj<C:
                if arr[ni-ddi[k]][nj-ddj[k]] != -1:
                    arr[ni - ddi[k]][nj - ddj[k]] = arr[ni][nj]
                arr[ni][nj] = 0
                ni += ddi[k]
                nj += ddj[k]
            else:
                ni -= ddi[k]
                nj -= ddj[k]
                break
    arr[start][0], arr[start][1] = -1, 0
    arr[start+1][0], arr[start+1][1] = -1, 0


ans = sum(map(sum, arr))+2
print(ans)