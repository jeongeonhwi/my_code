import sys
input = sys.stdin.readline

N = list(input())
N.pop()
ncnt = len(N)
acnt = N.count('a')
bcnt = N.count('b')
cnt = 0
check = False

while True:
    for i in range(ncnt):
        bcheck = False
        if N[i] == 'b':
            for j in range(bcnt):
                if N[(i+j)%ncnt] != 'b':
                    break
            else:
                bcheck = True
        if bcheck:
            check = True
            break
    if check:
        break
    cnt += 1


print(cnt)