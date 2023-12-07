import sys
sys.stdin = open('input.txt', 'r')



def permutation(start, end, k):
    global ans
    if ans != -1:
        return
    if start == k:
        check = 0
        for p in point:
            if (p[0],p[1]+2) in point:
                return
            elif (p[0],p[1]-2) in point:
                return
            arr[p[0]][p[1]] = 1
        jcheck = False
        for j in range(2*N):
            visited = [[0] * (N + N) for _ in range(2 * H + 1)]
            if arr[0][j] == 1:
                ni,nj=0,j
                visited[ni][nj] = 1
                while True:
                    if ni>=2*H:
                        if nj == j:
                            check+=1
                        else:
                            jcheck = True
                        break
                    for di,dj in [(0,-1),(0,1),(1,0)]:
                        tmpi,tmpj = ni+di,nj+dj
                        if 0<=tmpi<(2*H+1) and 0<=tmpj<(2*N):
                            if arr[tmpi][tmpj] == 1 and visited[tmpi][tmpj] == 0:
                                visited[tmpi][tmpj] = 1
                                ni,nj=tmpi,tmpj
                                break
            if jcheck:
                break
            if check == N:
                break
        if check == N:
            ans = m
            return
        for p in point:
            arr[p[0]][p[1]] = 0
        return
    for j in range(end):
        if used[j] == 0:
            point[start] = num[j]
            used[j] = 1
            permutation(start+1, end, k)
            used[j] = 0



N, M, H = map(int, input().split())
arr = [[0]*(N+N) for _ in range(2*H+1)]
for i in range(2*H+1):
    for j in range(2*N):
        if j%2==1:
            arr[i][j] = 1
for _ in range(M):
    a,b = map(int, input().split())
    arr[2*(a)-1][2*b] = 1
for i in arr:
    print(i)
num = []
for i in range(2*H):
    for j in range(2*N):
        if j != 0 and i%2==1 and j%2==0:
            if arr[i][j] == 1:
                continue
            if arr[i][j-2] != 1:
                if j+2>=2*N:
                    num.append((i,j))
                elif arr[i][j+2] != 1:
                    num.append((i,j))
end = len(num)
ans = -1
for m in range(4):
    used = [0]*end
    point = [0]*m
    permutation(0,end,m)
    if ans != -1:
        break
print(ans)

