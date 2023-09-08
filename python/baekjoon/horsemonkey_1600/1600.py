'''
원숭이가 말처럼 뛰는 경우의 수를 어떻게 줘야할지 모르겠음
visited를 1씩 더해서 계단식으로 접근해야 하나...
'''



import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

def bfs(start):
    visited = [[0]*W for _ in range(H)]
    q = []
    q.append(start)
    q = deque(q)
    visited[0][0] = 1
    while q:
        i, j = q.popleft()
        if i == H-1 and j == W-1:
            # print(visited)
            return visited[i][j]-1
        for k in range(12):
            ni = i+di[k]
            nj = j+dj[k]
            if 0<=ni<H and 0<=nj<W and visited[ni][nj] == 0 and arr[ni][nj] != 1:
                q.append((ni,nj))
                visited[ni][nj] = visited[i][j]+1
    else:
        return -1
    




di = [1, -1, 0, 0, -2, -1, -2, -1, 1, 2, 2, 1]
dj = [0, 0, 1, -1, -1, -2, 1, 2, -2, -1, 1, 2]

K = int(input())
W, H = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(H)]
ans = bfs((0,0))
if ans == -1:
    print(ans)
else:
    print(W+H-2-K*2)