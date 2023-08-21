# python

스택
-------
### pop, append를 사용하지 않는 버전, 차후 다른 언어와의 공통성을 위해
```python
#계산기2
'''
6528-*2/+
'''

stack = [0]*100
top = -1
s = str(input())
for x in s:
    # 피연산자면...
    if x not in '+-/*':
        # push(x)
        top += 1
        stack[top] = int(x)
    else:
        # pop()
        op2 = stack[top]
        top -= 1
        # pop()
        op1 = stack[top]
        top -= 1
        if x == '+':    # op1 + op2
            top += 1
            stack[top] = op1 + op2
        elif x == '-':
            top += 1
            stack[top] = op1 - op2
        elif x == '/':
            top += 1
            stack[top] = op1 / op2
        elif x == '*':
            top += 1
            stack[top] = op1 * op2
print(stack[0])



#계산기1
'''
(6+5*(2-8)/2)
'''
stack = [0]*100
top = -1
icp = {'(':3, '*':2, '/':2, '+':1, '-':1}
isp = {'(':0, '*':2, '/':2, '+':1, '-':1}

fx = str(input())
susik = ''
for x in fx:
    if x not in '(+-*/)':
        susik += x
    elif x == ')':
        while stack[top] != '(':    #peek
            susik += stack[top]
            top -= 1
        top -= 1    # '(' 버림 .pop
    else:
        # 토큰의 우선순위가 더 높으면
        if top==-1 or isp[stack[top]] < icp[x]:
            top += 1     #push
            stack[top] = x
        elif isp[stack[top]] >= icp[x]:
            while top > -1 and isp[stack[top]] >= icp[x]:
                susik += stack[top]
                top -= 1
            top += 1
            stack[top] = x
print(susik)
```



Queue
------
### Queue front, rear 방식, 일자 막대 형식
```python
def enQ(data):
    global rear
    rear += 1
    Q[rear] = data

def deQ():
    global front
    if front == rear:
        print('큐가 비어있음')
        return -1
    else:
        front += 1
        return Q[front]

Qsize = 3
Q = [0] * Qsize
rear = -1
front = -1
enQ(1)
enQ(2)
rear += 1
Q[rear] = 3
print(Q)
while front != rear:
    front += 1
    print(Q[front])

enQ(4)
print(deQ())
print(deQ())
print(deQ())
print(deQ())
```


### 선형형태의 큐, 원형 형태로 뺑글뺑글 돔

```python
def enq(data):
    global rear
    global front
    if (rear+1)%cQsize==front:
        front = (front+1)%cQsize
    rear = (rear+1)%cQsize
    cQ[rear] = data


def deq():
    global front
    tmp = cQ[front]
    front = (front+1)%cQsize
    return tmp


cQsize = 4
cQ = [0]*cQsize
front = 0
rear = 0

enq(1)
enq(2)
enq(3)
enq(4)
print(deq())
print(deq())
print(deq())
print(deq())
```



### BFS

그래프를 탐색하는 방법에는 크게 두 가지가 있음
1. 깊이 우선 탐색(DFS)
2. 너비 우선 탐색(BFS)

인접한 정점들에 대해 탐색을 한 후, 차례로 다시 너비우선탐색을 진행해야 하므로, 선입선출 형태의 자료구조인 큐를 활용함

```python
#너비 우선탐색 길찾기

'''
연결되 있는 두개의 정점 사이의 간선을 순서대로 나열해 놓은 것이다. 모든 정점을
 너비우선탐색하여 출력하시오. 시작 정점을 1로 시작하시오.
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

def bfs(s, V):  # 시작정점 s, 마지막 정점 V
    # visited 생성
    visited = [0] * (V+1)
    # 큐 생성
    q = []
    # 시작점 인큐
    q.append(s)
    # 시작점 방문표시
    visited[s] = 1
    # 큐에 정점이 남아있으면 front != rear
    while q:
        t = q.pop(0)
        print(t)    # 방문한 정점에서 할일
        for w in adj_l[t]:            # 인접한 정점 중 인큐되지 않은 정점 w가 있으면
            if visited[w]==0:               # w 인큐, 인큐되었음을 표시
                q.append(w)
                visited[w] = visited[t] +1



def bfs2(s, V):  # 시작정점 s, 마지막 정점 V
    # visited 생성
    visited = [0] * (V+1)
    # 큐 생성
    q = []
    # 시작점 인큐
    q.append(s)
    # 시작점 방문표시
    visited[s] = 1
    # 큐에 정점이 남아있으면 front != rear
    while q:
        t = q.pop(0)
        print(t)    # 방문한 정점에서 할일
        for w in range(1, V+1):            # 인접한 정점 중 인큐되지 않은 정점 w가 있으면
            if adj_m[t][w]==1 and visited[w]==0:               # w 인큐, 인큐되었음을 표시
                q.append(w)
                visited[w] = visited[t] +1






V, E = map(int, input().split())
arr = list(map(int, input().split()))
#인접리스트-----------------------
adj_l = [[] for _ in range(V+1)]
for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    adj_l[v1].append(v2)
    adj_l[v2].append(v1)
# 여기까지 인접리스트 -------------------
# bfs(1, 7)

# 인접행렬방식----------------------
adj_m = [[0]*(V+1) for _ in range(V+1)]
for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    adj_m[v1][v2] = 1
    adj_m[v2][v1] = 1  # 방향이 없는 경우
# 여기까지가 인접행렬방식--------------
bfs2(2, V)
```

### Queue 미로를 찾는 연습문제
```python
# 5105. [파이썬 S/W 문제해결 기본] 6일차 - 미로의 거리
'''
문제          답 : 5
1
5
13101
10101
10101
10101
10021
'''
def bfs(sti, stj, N):
    visited = [[0]*N for _ in range(N)]# visited생성
    q = []                              # 큐 생성
    q.append((sti, stj))                # 시작점 인큐
    visited[sti][stj] = 1               # 시작점 인큐 표시
    while q:                            # 큐가 비워질때 까지
        i, j = q.pop(0)                 # 디큐
        if maze[i][j] == 3:             # 처리
            return visited[i][j] -2     # 지나온 칸 수 리턴
        # 인접하고 인큐된 적이 없으면
        # 인큐, 인큐표시
        for di, dj in [[0,1], [1,0], [0,-1], [-1, 0]]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N and maze[ni][nj] !=1 and visited[ni][nj]==0:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] +1
    return 0                            # 3인칸에 도달할 수 없는 경우


def find_start(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j]==2:
                return i, j

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    sti, stj = find_start(N)
    ans = bfs(sti, stj, N)
    print(f'#{tc} {ans}')
```


순열
---------
```python
#교수님 써머리 백트래킹 재귀사용 순열

arr = [0,1,2,3,4,5,6,7,8,9]
N = len(arr)

def permutation(idx):
    # 종료 조건
    if idx == N:
        print(arr)
        return
    for swap_idx in range(idx, N):    # 바꿀 위치를 반복
        global count
        count += 1
        arr[idx], arr[swap_idx] = arr[swap_idx], arr[idx]
        permutation(idx+1)    # 다음 자리 확인
        arr[swap_idx], arr[idx] = arr[idx], arr[swap_idx]   #원상 복구 (처음 모양에서 또 자리를 바꾸기 때문에 결과를 예측하기 어려워 지고 잘못된 동작을 수행하게 된다.)
        # arr[idx], arr[swap_idx] = arr[swap_idx], arr[idx]

count = 0
permutation(0)
print(count)
```


트리
------------------------
용어정리

1. 노드의 차수:노드에 연결된 자식노드의 수

2. 트리의 차수:트리에 있는 노드의 차수 중에서 가장 큰 값

3. 단말노드(리프 노드):차수가 0인 노드. 자식 노드가 없는 노드


### 포화 이진 트리

모든 레벨에 노드가 포화상태로 차 있는 이진 트리

높이가 h일 때, 최대의 노드 개수인 (2^(h+1)-1)의 노드를 가진 이진 트리

- 높이 3일 때 15개의 노드

루트를 1번으로 하여 2^(h+1)-1까지 정해진 위치에 대한 노드 번호를 가짐


### 순회 : 트리의 노드들을 체계적으로 방문하는 것

3가지의 기본적인 순회방법

1. 전위순회 : VLR
    - 부모노드 방문 후, 자식노드를 좌,우 순서로 방문한다.

2. 중위순회 : LVR
    - 왼쪽 자식노드, 부모노드, 오른쪽 자식노드 순으로 방문한다.

3. 후위순회 : LRV
    - 자식노드를 좌우 순서로 방문한 후, 부모노드로 방문한다.


1. 전위 순회
    1. 현재 노드n을 방문하여 처리한다. -> V
    2. 현재 노드n의 왼쪽 서브트리로 이동한다. -> L
    3. 현재 노드n의 오른쪽 서브트리로 이동한다. -> R

```python
#전위 순회 알고리즘
def preorder_traverse(T):
    if T:
        visit(T)
        preorder_traverse(T.left)
        preorder_traverse(T.right)
```

2. 중위 순회
    1. 현재 노드n의 왼쪽 서브트리로 이동한다. -> L
    2. 현재 노드n을 방문하여 처리한다. -> V
    3. 현재 노드n의 오른쪽 서브트리로 이동한다. -> R

```python
#중위 순회 알고리즘
def inorder_traverse(T):
    if T:
        inorder_traverse(T.left)
        visit(T)
        inorder_traverse(T.right)
```

3. 후위 순회
    1. 현재 노드n의 왼쪽 서브트리로 이동한다. -> L
    2. 현재 노드n의 오른쪽 서브트리로 이동한다. -> R
    3. 현재 노드n을 방문하여 처리한다. -> V

```python
#후위 순회 알고리즘
def postorder_traverse(T):
    if T:
        postorder_traverse(T.left)
        postorder_traverse(T.right)
        visit(T)
```

