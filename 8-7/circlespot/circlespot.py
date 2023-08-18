import sys
sys.stdin = open("input.txt")


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    xlist = []
    count = 0
    for i in range(N+1):
        xlist.append(i)
    ylist = xlist[1:]
    for i in xlist:
        for j in ylist:
            if i**2 + j**2 <= N**2:
                count += 1
    result = count*4 +1
    print(f'#{tc} {result}')