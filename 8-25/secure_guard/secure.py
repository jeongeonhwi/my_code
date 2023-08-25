import sys
sys.stdin = open('input.txt', 'r')

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

def secure_area():
    for ii in range(K+K-1):
        for jj in range(K+K-1):
            pass


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    total = 0
    for i in range(N):
        for j in range(N):
            k = 0
            count = 0
            if arr[i][j] == 1:
                count+=1
            for k in range(4):
                ni = i+di[k]
                nj = j+dj[k]
                if 0<=ni<N and 0<=nj<N:
                    if arr[ni][nj] == 1:
                        count += 1

