import sys
sys.stdin = open('input.txt', 'r')


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
    for i in range(R):
        for j in range(C):
            for k in range(4):
                ni, nj = i+di[k], j+dj[k]
                if 0<=ni<R and 0<=nj<C and arr[ni][nj] != -1:
                    arr[ni][nj] += arr[i][j]//5
                    arr[i][j] -= arr[i][j]//5
    upi, upj = start, 0
    for k in range(4):
        while True:


ans = sum(map(sum, arr))+2
print(ans)