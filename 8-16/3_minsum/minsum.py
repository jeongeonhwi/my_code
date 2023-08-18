import sys
sys.stdin = open('input.txt')

def f(idx):
    if idx <= len(nlist):
        global count
        global min_v
        count = 0
        for i in range(idx):
            count += arr[i][nlist[i]]
            if min_v <= count:
                return
    if idx == len(nlist):
        count = 0
        for i in range(len(nlist)):
            count += arr[i][nlist[i]]
            if min_v <= count:
                return
        if min_v > count:
            min_v = count
            return
        else:
            return
    for sidx in range(idx, len(nlist)):
        nlist[idx], nlist[sidx] = nlist[sidx], nlist[idx]
        f(idx+1)
        nlist[sidx], nlist[idx] = nlist[idx], nlist[sidx]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    nlist = [i for i in range(N)]
    min_v = 0
    for i in range(N):
        min_v += arr[i][i]
    f(0)
    print(f'#{tc} {min_v}')

