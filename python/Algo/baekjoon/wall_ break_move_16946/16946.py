import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

def dfs(si,sj):
    stack = [(si,sj)]
    visited[si][sj][0] = 1
    stack_set = set()
    stack_set.add((si,sj))
    while stack:
        i,j = stack.pop()
        for ni,nj in [[i+1,j],[i,j+1],[i-1,j],[i,j-1],]:
            if 0<=ni<N and 0<=nj<M and visited[ni][nj][0] == 0 and arr[ni][nj] == '0':
                visited[ni][nj][0] = 1
                stack.append((ni,nj))
                stack_set.add((ni,nj))
    cnt = len(stack_set)
    for i,j in stack_set:
        visited[i][j][0] = cnt
        visited[i][j][1] = label

N,M = map(int, input().split())
arr = [list(input().strip()) for _ in range(N)]
visited = [[[0,0] for _ in range(M)] for _ in range(N)]
label = 0
for i in range(N):
    for j in range(M):
        if visited[i][j][0] == 0 and arr[i][j] == '0':
            label += 1
            dfs(i,j)
for i in range(N):
    for j in range(M):
        cnt = 1
        if arr[i][j] == '1':
            label_set = set()
            for ni,nj in [[i+1,j],[i,j+1],[i-1,j],[i,j-1],]:
                if 0<=ni<N and 0<=nj<M and arr[ni][nj] == '0':
                    if visited[ni][nj][1] in label_set:
                        continue
                    label_set.add(visited[ni][nj][1])
                    cnt += visited[ni][nj][0]
            arr[i][j] = cnt%10
        print(arr[i][j], end='')
    print()