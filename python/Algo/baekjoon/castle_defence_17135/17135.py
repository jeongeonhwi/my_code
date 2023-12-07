import sys
# sys.stdin = open('input.txt', 'r')

import copy
from collections import deque
# 가장 가깝고 가장 왼쪽의 적부터 제거해야 하므로 bfs 사용
def bfs(p):
    visited = [[0]*M for _ in range(N)]
    visited[N-1][p] = 1
    q = [(N-1,p)]
    q = deque(q)
    while q:
        i,j = q.popleft()
        # 만약 사정거리보다 bfs가 길어지면 함수종료
        if visited[i][j] > D:
            return 0
        # 적을 발견하면 그좌표만 꺼냈다.
        # 왜냐하면 같은 적을 다른 궁수도 쏠 수 있기때문에
        # 좌표 체크만 해줌
        if arr[i][j]:
            return (i,j)
        # 델타탐색 방향은 왼쪽부터 위쪽 오른쪽으로 간다.
        for k in [(0,-1),(-1,0),(0,1)]:
            ni, nj = i+k[0], j+k[1]
            if 0<=ni<N and 0<=nj<M:
                visited[ni][nj] = visited[i][j]+1
                q.append((ni,nj))



N,M,D = map(int, sys.stdin.readline().split())
arr2 = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
number = [i for i in range(M)]
# 처음에는 순열로 궁수 위치를 추출했는데 비트연산이 더빠를것 같아서
# 변경하였음
my_set = set()
for i in range(1<<M):
    tmp = set()
    for j in range(M):
        if len(tmp) > 2:
            break
        if i&(1<<j):
            tmp.add(number[j])
    tmp = tuple(tmp)
    if len(tmp) == 3:
        my_set.add(tmp)
max_v = 0
for i in my_set:
    arr = copy.deepcopy(arr2)
    cnt = 0
    while True:
        check = 0
        for c in arr:
            check += c.count(1)
        if not check:
            max_v = max(max_v, cnt)
            break
        my_set = set()
        for p in i:
            r = bfs(p)
            if r != 0:
                my_set.add(r)
        for my in my_set:
            arr[my[0]][my[1]] = 0
        cnt += len(my_set)
        for n in range(N-1, -1, -1):
            if n == N-1:
                arr[n] = [0]*M
            else:
                arr[n+1] = arr[n]
                arr[n] = [0]*M
print(max_v)