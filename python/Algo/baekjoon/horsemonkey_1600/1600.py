'''
원숭이가 말처럼 뛰는 경우의 수를 어떻게 줘야할지 모르겠음
visited를 1씩 더해서 계단식으로 접근해야 하나...
'''
import sys
sys.stdin = open('input.txt', 'r')




from collections import deque

def bfs():
    visited = [[int(1e9)]*W for _ in range(H)]
    # horse = [[0]*W for _ in range(H)]
    q = []
    q.append((0, 0, 0, 0))
    q = deque(q)
    visited[0][0] = 0
    while q:
        i, j, h, cnt = q.popleft()
        if i == H-1 and j == W-1:
            return cnt
        for k in range(4):
            ni = i+di[k]
            nj = j+dj[k]
            if 0<=ni<H and 0<=nj<W and visited[ni][nj] > h and arr[ni][nj] != 1:
                q.append((ni,nj, h, cnt+1))
                visited[ni][nj] = h
        for hh in range(8):
            nni = i+hi[hh]
            nnj = j+hj[hh]
            if 0 <= nni < H and 0 <= nnj < W and arr[nni][nnj] != 1 and visited[nni][nnj] > h+1:
                if h < K:
                    visited[nni][nnj] = h+1
                    q.append((nni, nnj, h+1, cnt+1))
    else:
        return -1




hi = [ -2, -1, -2, -1, 1, 2, 2, 1]
hj = [ -1, -2, 1, 2, -2, -1, 1, 2]
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

K = int(input())
W, H = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(H)]
ans = bfs()
# for i in ans:
#     print(i)
print(ans)