t  = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())
    apt = [[0]*n for _ in range(k+1)]
    for i in range(n):
        apt[0][i] = i+1
    for i in range(k+1):
        apt[i][0] = 1
    for i in range(1, k+1):
        for j in range(1,n):
            apt[i][j] = apt[i-1][j]+apt[i][j-1]
    print(apt[k][n-1])