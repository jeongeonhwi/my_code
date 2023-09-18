import sys
sys.stdin = open('input.txt', 'r')

black = 'BWBWBWBW'
white = 'WBWBWBWB'

N, M = map(int, input().split())
arr = [input() for _ in range(N)]
cN, cM = N-8, M-8
min_v = N*M
for i in range(cN+1):
    for j in range(cM+1):
        cntb = 0
        cntw = 0
        for ii in range(4):
            for jj in range(8):
                if arr[i+ii*2][j+jj] != black[jj]:
                    cntb += 1
                if arr[i+ii*2+1][j+jj] != white[jj]:
                    cntb += 1
                if arr[i+ii*2][j+jj] != white[jj]:
                    cntw += 1
                if arr[i+ii*2+1][j+jj] != black[jj]:
                    cntw += 1
        tmp = min(cntw, cntb)
        min_v = min(tmp, min_v)
print(min_v)

