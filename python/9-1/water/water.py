import sys
sys.stdin = open('input.txt', 'r')

def find_water(arr):
    waterlist = []
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'W':
                count = 0
                for k in range(4):
                    if 0<=i+di[k]<N and 0<=j+dj[k]<M:
                        if arr[i+di[k]][j+dj[k]] =='W':
                            count += 1
                    else:
                        count += 1
                if count != 4:
                    waterlist.append((i,j))
    return waterlist


def enq(data):
    global rear
    rear += 1
    q[rear] = data


def deq():
    global front
    if front == rear:
        return ('end', 'end')
    else:
        front += 1
        return q[front]



def bfs(arr):
    while True:
        i, j = deq()
        if i == 'end':
            break
        for k in range(4):
            ni = i+di[k]
            nj = j+dj[k]
            if 0<=ni<N and 0<=nj<M:
                if arr[ni][nj] == 'L':
                    if visited[i][j]+1<visited[ni][nj] or visited[ni][nj] ==0:
                        enq((ni, nj))
                        visited[ni][nj] = visited[i][j]+1
    return



di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    waterlist = find_water(arr)
    visited = [[0] * M for _ in range(N)]
    q = [0]*(N*M)

    # print(waterlist)
    # for i in range(len(waterlist)):
    rear = -1
    front = -1
    while waterlist:
        enq(waterlist.pop())
    bfs(arr)
    total = 0
    for i in range(N):
        for j in range(M):
            total += visited[i][j]
    print(f'#{tc} {total}')