import sys
sys.stdin = open('input.txt', 'r')

def dfs(si,sj):
    stack = [(si,sj)]
    cnt = 0
    while stack:
        i,j = stack.pop()
        if arr[i][j] == '1':
            arr[i][j] = '0'
            cnt += 1
        for di,dj in [(0,1),(1,0),(0,-1),(-1,0)]:
            ni,nj = i+di,j+dj
            if 0<=ni<N and 0<=nj<N and arr[ni][nj] == '1':
                stack.append((ni,nj))
    # for i in arr:
    #     print(i)
    # print(cnt)
    # print()

    return cnt



N = int(input())
arr = [list(input()) for _ in range(N)]
cnt = 0
alist = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == '1':
            tmp = dfs(i,j)
            alist.append(tmp)
            cnt+=1
print(cnt)
alist.sort()
for i in alist:
    print(i)