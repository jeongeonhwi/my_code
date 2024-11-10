M,N,K = map(int, input().split())
arr = [[0]*N for _ in range(M)]
for _ in range(K):
    x1,y1,x2,y2 = map(int, input().split())
    for x in range(x1,x2):
        for y in range(y1,y2):
            arr[y][x] = 1
def dfs(si,sj):
    stack = [(si,sj)]
    arr[si][sj] = 1
    cnt = 1
    while stack:
        i,j = stack.pop()
        for ni,nj in [(i+1,j),(i,j+1),(i-1,j),(i,j-1),]:
            if 0<=ni<M and 0<=nj<N and arr[ni][nj] == 0:
                arr[ni][nj] = 1
                cnt+=1
                stack.append((ni,nj))
    return cnt
al = []
for m in range(M):
    for n in range(N):
        if arr[m][n] == 0:
            al.append(dfs(m,n))
print(len(al))
print(*al)