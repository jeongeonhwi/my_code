import sys
# sys.stdin = open('input.txt', 'r')

def dfs(arr):
    q = [(0,0,arr[0][0])]
    max_len = 0
    while q:
        i, j, m = q.pop()
        for k in range(4):
            ni, nj = i+di[k], j+dj[k]
            if 0<=ni<R and 0<=nj<C:
                if arr[ni][nj] not in m:
                    tmpm = m+arr[ni][nj]
                    q.append((ni,nj,tmpm))
                    max_len = max(max_len, len(tmpm))
    return max_len

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
R, C = map(int, input().split())
arr = [sys.stdin.readline() for _ in range(R)]
ans = dfs(arr)
if not ans:
    ans = 1
print(ans)