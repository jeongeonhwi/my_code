import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

def dfs(si,sj):
    global flag
    stack = [(si,sj)]
    visited[si][sj] = (si,sj)
    check = 1
    while stack:
        i,j = stack.pop()
        for ni,nj in [(i+1,j),(i,j+1),(i-1,j),(i,j-1),]:
            if 0<=ni<12 and 0<=nj<6 and visited[ni][nj] == 0 and arr[si][sj] == arr[ni][nj]:
                stack.append((ni,nj))
                visited[ni][nj] = (si,sj)
                check += 1
    if check >= 4:
        flag = False
        stack = [(si,sj)]
        visited[si][sj] = 1
        arr[si][sj] = '.'
        while stack:
            i, j = stack.pop()
            for ni, nj in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1), ]:
                if 0 <= ni < 12 and 0 <= nj < 6 and visited[ni][nj] == (si,sj):
                    stack.append((ni, nj))
                    visited[ni][nj] = 1
                    arr[ni][nj] = '.'

arr = [list(input().strip()) for _ in range(12)]
ans = 0
while True:
    flag = True
    visited = [[0]*6 for _ in range(12)]
    for i in range(12):
        for j in range(6):
            if arr[i][j] == '.' or visited[i][j] != 0:
                continue
            dfs(i,j)
    # for i in arr:
    #     print(i)

    if flag:
        break
    ans += 1
    for i in range(10, -1, -1):
        for j in range(6):
            if arr[i][j] != '.':
                tmp = arr[i][j]
                arr[i][j] = '.'
                go = 1
                while True:
                    if arr[i+go][j] != '.':
                        arr[i+go-1][j] = tmp
                        break
                    if i+go == 11:
                        arr[i+go][j] = tmp
                        break
                    go += 1

print(ans)