'''
문제스타일 : 최소거리를 찾아가는 문제이기 때문에 bfs를 while문으로
최소거리를 찾으면 0으로 바꾸고 더이상 먹이가 없을때까지 while 반복함.
접근 1. 단순히 di,dj로 접근하면 반례가 있음.
접근 2. 가장 가까운 위치들을 모두 리스트에 담고 그 리스트중 가장 위쪽과 왼쪽
위치를 추출함.
접근 3. while 문이 반복되어 bfs가 한번 돌면 먹이+1 해주고 만약 먹이가
크기와 동일해지면 먹이 = 0 해주고 크기 +1 해줌
접근 4. bfs가 먹이를 못찾고 돌아오면 while문을 종료해줌
'''



import sys
sys.stdin = open('input.txt', 'r')

from collections import deque
def bfs(bi,bj, size):
    visited = [[0]*N for _ in range(N)]
    q = [(bi,bj, size)]
    visited[bi][bj] = 1
    q = deque(q)
    tmplist = []
    tmplv = 0
    while q:
        i,j,s = q.popleft()
        for k in range(4):
            ni,nj = i+di[k], j+dj[k]
            if 0<=ni<N and 0<=nj<N and visited[ni][nj] == 0 and arr[ni][nj] <= s:
                if arr[ni][nj] != 0 and arr[ni][nj] < s:
                    if tmplv == 0:
                        tmplist.append((ni, nj))
                        tmplv = visited[i][j]
                    elif tmplv == visited[i][j]:
                        tmplist.append((ni, nj))
                else:
                    visited[ni][nj] = visited[i][j] + 1
                    q.append((ni,nj,s))
                    if tmplv == 0:
                        continue
                    if visited[ni][nj] == tmplv+1:
                        continue
                    tmplist.sort()
                    if len(tmplist) >=2:
                        if tmplist[0][0] == tmplist[1][0]:
                            if tmplist[0][1] < tmplist[1][1]:
                                arr[tmplist[0][0]][tmplist[0][1]] = 0
                                return tmplv, tmplist[0]
                            else:
                                arr[tmplist[1][0]][tmplist[1][1]] = 0
                                return tmplv, tmplist[1]
                        arr[tmplist[0][0]][tmplist[0][1]] = 0
                        return tmplv, tmplist[0]
                    arr[tmplist[0][0]][tmplist[0][1]] = 0
                    return tmplv, tmplist[0]
    if tmplv != 0:
        tmplist.sort()
        if len(tmplist) >= 2:
            if tmplist[0][0] == tmplist[1][0]:
                if tmplist[0][1] < tmplist[1][1]:
                    arr[tmplist[0][0]][tmplist[0][1]] = 0
                    return tmplv, tmplist[0]
                else:
                    arr[tmplist[1][0]][tmplist[1][1]] = 0
                    return tmplv, tmplist[1]
            arr[tmplist[0][0]][tmplist[0][1]] = 0
            return tmplv, tmplist[0]
        arr[tmplist[0][0]][tmplist[0][1]] = 0
        return tmplv, tmplist[0]
    return 0, (100,100)

def find_baby(arr):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 9:
                return (i,j)


di = [-1, 0, 0, 1]
dj = [0, -1, 1, 0]
N = int(input())
# 가장처음 아기상어의 크기는 2
# 자기보다 큰 물고기 칸은 지날 수 없고 크기가 같은 물고기는 먹을 수 없고 지나갈 순 있다.
arr = [list(map(int, input().split())) for _ in range(N)]
baby = find_baby(arr)
arr[baby[0]][baby[1]] = 0
size = 2
eat_fish = 0
tm = 0
while True:
    tmp, p = bfs(baby[0], baby[1], size)
    # print(p, size)
    # for i in arr:
    #     print(i)
    # print()
    if tmp == 0:
        break
    else:
        baby = p
        tm+=tmp
        eat_fish += 1
        if eat_fish == size:
            eat_fish = 0
            size += 1
print(tm)