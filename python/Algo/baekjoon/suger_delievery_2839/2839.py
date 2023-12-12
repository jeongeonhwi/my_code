import sys
input = sys.stdin.readline

N = int(input())

cnt = N

five = N//5+1
check = False
for i in range(five, -1, -1):
    if i*5 == N:
        cnt = i
        break
    for j in range(1, N):
        if i*5 + j*3 == N:
            cnt = i+j
            check = True
            break
    if check:
        break

if cnt == N:
    print(-1)
else:
    print(cnt)