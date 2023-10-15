N, M, H = map(int, input().split())
arr = [[0]*(N+N) for _ in range(2*H+1)]
for i in range(2*H+1):
    for j in range(2*N):
        if j%2==1:
            arr[i][j] = 1
for _ in range(M):
    a,b = map(int, input().split())
    arr[2*(a)-1][2*b] = 1

