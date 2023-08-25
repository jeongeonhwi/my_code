# python

스택
-------
### pop, append를 사용하지 않는 버전, 차후 다른 언어와의 공통성을 위해
```python
#계산기2 (후위계산법)
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



#계산기1 (후위계산법)
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

이진 탐색 트리
* 탐색작업을 효울적으로 하기 위한 자료구조
* 모든 원소는 서로 다른 유일한 키를 갖는다.
* 왼쪽 서브트리< 루트 노드 < 오른쪽 서브트리
* 왼쪽 서브트리와 오른쪽 서브트리도 이진 탐색 트리다.
* 중위 순회하면 오름차순으로 정렬된 값을 얻을 수 있다.

1. 삽입 연산
    1. 먼저 탐색 연산을 수행
        - 삽입할 원소와 같은 원소가 트리에 있으면 삽입할 수 없으므로, 같은 원소가 트리에 있는지 탐색하여 확인한다.
        - 탐색에서 탐색 실패가 결정되는 위치가 삽입 위치가 된다.
    2. 탐색 실패한 위치에 원소를 삽입한다.

### 힙(heap)
완전 이진 트리에 있는 노드 중에서 키값이 가장 큰 노드나 키값이 가장 작은 노드를 찾기 위해서 만든 자료구조

1. 최대 힙(max heap)
    * 키 값이 가장 큰 노드를 찾기 위한 **완전 이진 트리**
2. 최소 힙(min heap)
    * 키 값이 가장 작은 노드를 찾기 위한 **완전 이진 트리**

### 힙 삽입
1. 완전 이진 트리를 지키기 위해 가장 끝에 넣는다.
2. 그후 최대 힙인지 최소힙인지에 따라 부모노드와 비교하여 위치를 결정한다.

```python
# 최소 힙 삽입하는법
data = [3, 7, 9, 2, 1, 5]   # 삽입할 데이터 하나씩 반복문으로 넣을 예정
N = 6   # 데이터의 길이

heap = [0]*(N+1)    # 0번 인덱스는 사용x
last_idx = 1        # 가장 마지막 위치(초기화 root 인덱스)

# heap 에다가 넣어 봅시다.
for idx in range(N):
    if not heap[last_idx]:   # root 인덱스
        heap[last_idx] = data[idx]
    else:
        last_idx += 1   # 들어갈 인덱스 위치
        heap[last_idx] = data[idx]  # 마지막 위치에 값을 삽입

        # 우선순위 비교를 위한 준비
        parent = last_idx//2    # 부모 노드 인덱스
        child = last_idx        # 알아보기 쉽게 변수명을 지정

        while heap[parent] > heap[child]:
            # 부모 노드와 자식 노드를 교체
            heap[parent], heap[child] = heap[child], heap[parent]
            # 다음 부모노드와 자식 노드를 지정
            child = parent
            parent = child//2
print(heap)
```

### 힙 삭제
1. 힙에서는 루트 노드의 원소만을 삭제할 수 있다.
2. 루트 노드의 원소를 삭제하여 반환한다.
3. 힙의 종류에 따라 최대값 또는 최소값을 구할 수 있다.
```python
# 힙(heap) 삭제하는 법
def deq():
    global last
    tmp = heap[1]           # 루트 백업
    heap[1] = heap[last]    # 삭제할 노드의 키를 루트에 복사
    last -= 1               # 마지막 노드 삭제
    p = 1       # 루트에 옮긴 값을 자식과 비교
    c = p*2     # 왼쪽 자식 (비교할 자식노드 번호)
    while c <= last:        # 자식이 하나라도 있으면....
        if c+1 <= last and heap[c] < heap[c+1]:  # 오른쪽 자식도 있고, 오른쪽 자식이 더 크면...
            c += 1      # 비교 대상이 오른쪽 자식노드
        if heap[p] < heap[c]:   # 자식이 더 크면 최대합 규칙에 어긋나므로
            heap[p], heap[c] = heap[c], heap[p]
            p = c       # 자식을 새로운 부모로
            c = p*2     # 왼쪽 자식 번호를 계산
        else:       # 부모가 더 크면
            break   # 비교 중단,

    return tmp

heap = [0]*100
last = 0
```

비트
----------
비트연산자
1. & : 비트단위로 and연산을 한다.
2. | : 비트단위로 or연산을 한다.
3. ^ : 비트단위로 xor연산을 한다. (같으면 0 다르면 1)
4. ~ : 단항 연산자로서 피연산자의 모든 비트를 반전시킨다.
5. << : 피연산자의 비트 열을 왼쪽으로 이동시킨다.
6. >> : 피연산자의 비트 열을 오른쪽으로 이동시킨다.

비트연산
1. 1<<n
    * 2^n의 값을 갖는다.
    * 원소가 n개일 경우의 모든 부분집합의 수를 의미한다.
    * power set(모든 부분집합)
        - 공집합과 자기 자신을 포함한 모든 부분집합
        - 각 원소가 포함되거나 포함되지 않는 2가지 경우의 수를 계산하면 모든 부분집합의 수가 계산된다.
2. i&(1<<j)
    * 계산 결과는 i의 j번째 비트가 1인지 아닌지를 의미한다.


진수
-------
컴퓨터에서의 음의 정수 표현 방법
1. 1의 보수 : 부호와 절대값으로 표현된 값을 부호 비트를 제외한 나머지 비트들을 0은 1로, 1은 0으로 변환한다.
2. 2의 보수 : 1의 보수방법으로 표현된 값의 최하위 비트에 1을 더한다.

8-25