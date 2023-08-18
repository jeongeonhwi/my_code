import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())
    nlist = [0]*N
    for k in range(1, Q+1):
        a, b = map(int, input().split())
        for i in range(a-1, b):
            nlist[i] = k
    print(f'#{tc}', end=" ")
    for i in range(N):
        print(nlist[i], end=" ")
    print()