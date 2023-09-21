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
```python
def dfs(n, V, adj_arr):
    stack = []
    visit = [0]*(V+1)
    visit[n] = 1
    while True:
        for w in range(V+1):
            if adj_arr[n][w] == 1 and visit[w] == 0:
                stack.append(n)
                n = w
                visit[n] = 1
                break
        else:
            if stack:
                n = stack.pop()
            else:
                break
    return visit

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
```python
#순열 만드는 공식. 중간에 p값을 더해서 최소값보다 p값이 커진다면 재귀를 차단하여 연산값을 줄일 수 있음
def f(i, N, K):     # i 이전에 고른 개수, N개에서 K개를 고르는 순열
    if i ==K:       # 순열 완성 : k개르 ㄹ모두 고른 경우
        print(p)
        return
    else:       # p[i]에 들어갈 숫자를 결정
        for j in range(N):
            if used[j]==0:      # 아직 사용되기 전이면
                p[i] = card[j]
                used[j] = 1
                f(i+1, N, K)
                used[j] = 0


# card = list(map(int, input()))
card = [1, 2, 3, 4, 5]
N = 5       #N개의 숫자에서
K = 3       #K개를 골라 만드는 순열
used = [0]*N #이미 사용한 카드인지 표시
p = [0]*3
f(0, 5, 3)

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
```python
'''
부분집합생성방법 : 바이너리 카운팅
아주 중요한 내용!!!!!!!!!!!!!!!!!!!!
A형 1번문제 풀이 방법.
'''

arr = [3,6,7,1,5,4]
N = 6
for i in range(1,1<<N-1):   # //2를 하게 되면 중복되는 값도 없고 앞에 1덕분에 비어있는 집합도 없다.
    group1 = []             # 1<<(N-1) == (1<<N)//2
    group2 = []
    total1 = 0
    total2 = 0
    for j in range(N):
        if i&(1<<j):        # j번 비트가 0이 아니면
            group1.append(arr[j])
            total1 += arr[j]
        else:
            group2.append(arr[j])
            total2 += arr[j]
    r1 = f(group1)
    r2 = f(group2)
    if r1 and r2:
        if min_v > abs(total1-total2):
            pass

# 부분집합

```
```python
# 부분집합의 합을 구하는 문제
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    subset = []
    total = 0
    for i in range(1<<N):
        tmp = []
        for j in range(N):
            if i&(1<<j):
                tmp.append(arr[j])
        if sum(tmp) == K:
            total += 1
    print(f'#{tc} {total}')

```

진수
-------
컴퓨터에서의 음의 정수 표현 방법
1. 1의 보수 : 부호와 절대값으로 표현된 값을 부호 비트를 제외한 나머지 비트들을 0은 1로, 1은 0으로 변환한다.
2. 2의 보수 : 1의 보수방법으로 표현된 값의 최하위 비트에 1을 더한다.

# 컴퓨팅 사고력
--------
증명
- 증명은 정확한 명제식으로 표현할 수 있는 것이라야 함
- 보통은 정확한 명제식으로 쓰지 않으나 근본적으로는 명제식으로 바꿀 수 있음
- 증명에 대한 수많은 오해가 p->q를 p<->q와 혼동하는 것에서 일아남

n^2이 3의 배수이면 n은 3의 배수임을 증명하라.
- n**2 == 3k 이라면 n은 루트3k이므로 거짓
 
수와 표현
- 프로그램에서 log밑은 2이다.


# 순열
```python
def f(i, N, K):     # i 이전에 고른 개수, N개에서 K개를 고르는 순열
    if i ==K:       # 순열 완성 : k개를 모두 고른 경우
        print(p)
        return
    else:       # p[i]에 들어갈 숫자를 결정
        for j in range(N):
            if used[j]==0:      # 아직 사용되기 전이면
                p[i] = card[j]
                used[j] = 1
                f(i+1, N, K)
                used[j] = 0


# card = list(map(int, input()))
card = [1, 2, 3, 4, 5]
N = 5       #N개의 숫자에서
K = 3       #K개를 골라 만드는 순열
used = [0]*N #이미 사용한 카드인지 표시
p = [0]*3
f(0, 5, 3)

```

```python
# 자리를 바꿔줘면서 순열을 구하는 법
def my_perm(time, N):
    if time == N:
        if max_v < value:
            max_v = value
        return
    else:
        for i in range(N):
            for j in range(i+1, N):
                numbers[i], numbers[j] = numbers[j], numbers[i]
                my_perm(time+1, N)
                numbers[i], numbers[j] = numbers[j], numbers[i]

```
# 알고리즘 설계 기법의 종류
1. 전체를 다 보자 (BRute Force - 완전탐색)
    - 배열 : 반복문을 다 돌리기
    - 그래프 : DFS, BFS
2. 상황마다 좋은 걸 고르자 (Greedy - 탐욕)
    - 규칙을 찾는 것
    - 주의사항 : 항상 좋은 것을 뽑아도, 최종 결과가 제일 좋다고 보장되지 않는다.
3. 하나의 큰 문제를 작은 문제로 나누어 부분적으로 해결하자 (Dynamic Programming)
    - Memoization 기법을 활용
    - 점화식(bottom-up), 재귀(top-down)
4. 큰 문제를 작은 문제로 쪼개서 해결하자 (Divide and Conquer - 분할 정복)
5. 전체를 중, 가능성 없는 것을 빼고 보자(Backtracking - 백트래킹)
    - 가지치기
### 분할정렬 코드
```python
'''
재밌는점. if len(arr)==1으로 리턴이 나오지 않으면 뒤의 재귀식들이 대기한다.
그리고 리턴이 되면 그때 재귀식이 시작되어 올라간다.
'''

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    left = merge_sort(arr[:len(arr)//2])
    right = merge_sort(arr[len(arr)//2:])
    return merge(left, right)


def merge(left, right):
    global cnt
    result = left+right
    if left[-1] > right[-1]:
        cnt+=1
    idx = 0
    lidx = 0
    ridx = 0
    while len(left)>lidx and len(right)>ridx:
        if left[lidx] < right[ridx]:
            result[idx] = left[lidx]
            idx += 1
            lidx += 1
        elif left[lidx] > right[ridx]:
            result[idx] = right[ridx]
            idx += 1
            ridx += 1
        else:
            result[idx] = left[lidx]
            idx+= 1
            lidx+=1
            result[idx] = right[ridx]
            idx+=1
            ridx+=1
    if len(left) > lidx:
        while len(left) > lidx:
            result[idx] = left[lidx]
            idx+= 1
            lidx+=1
    else:
        while len(right) > ridx:
            result[idx] = right[ridx]
            idx += 1
            ridx += 1
    return result

```
### 퀵정렬 코드
```python
def quick(lst, s, e):
    if s < e:
        a = partition(lst, s, e)
        quick(lst, s, a - 1)
        quick(lst, a + 1, e)
 
 
def partition(lst, s, e):
    p = lst[s]
    i = s
    j = e
    while i <= j:
        while i <= j and p >= lst[i]:
            i += 1
        while i <= j and p <= lst[j]:
            j -= 1
        if i < j:
            lst[i], lst[j] = lst[j], lst[i]
    lst[s], lst[j] = lst[j], lst[s]
    return j
```
### 이진 검색 **아주중요(코테단골문제)**
* 코딩 테스트의 메인 알고리즘 중 하나
* 목적 : 원하는 값을 빠리 찾는 것
* 시간 : O(logN)
* Parametric Search (이진 검색 심화 버전)
    - 특정 범위 검색
    - lower bound
    - upper bound
        - 여러 개의 데이터 중 2가 처음 나온 시점
        - 2~9 사이의 데이터는 몇개인가?
```python
'''
이진검색 - 반복문
문제에서 데이터가 정렬되어 있다 라는 조건이 없다면
반드시 정렬을 먼저 수행해야 한다.
첫번째 와일문으로 풀기
두번째 재귀로 풀기
'''

arr = [2, 4, 7, 9, 11, 19, 23]
arr. sort()

def binarySearch(target):
    low = 0
    high = len(arr) -1

    # low >= high 라면 데이터를 못찾은 경우
    while low <= high:
        mid = (low + high) // 2

        # 1. 가운데 값이 정답인 경우
        if arr[mid] == target:
            return mid
        # 2. 가운데 값이 정답보다 작은 경우
        elif arr[mid] < target:
            low = mid+1
        # 3. 가운데 값이 정답보다 큰 경우
        else:
            high = mid -1
    return '해당 데이터는 없습니다.'

# 함수 한번 호출 때마다 low, high 변수가 바뀌어서 사용됨
def binarySearch2(low, high, target):
    # 기저 조건: 언제까지 재귀호출을 반복할 것인가?
    # low > high 데이터를 못찾음
    if low > high:
        return '해당 데이터는 없습니다.'
    mid = (low+high)//2
    # 1. 가운데 값이 정답인 경우
    if arr[mid] == target:
        return mid
    # 2. 가운데 값이 정답보다 작은 경우
    elif arr[mid] < target:
        return binarySearch2(mid+1, high, target)
    # 3. 가운데 값이 정답보다 큰 경우
    else:
        return binarySearch2(low, mid-1, target)
```
### 백트래킹(Backtracking) 개념
여러가지 선택지들이 존재하는 상황에서 한가지를 선택한다.  
선택이 이루어지면 새로운 선택지들의 집합이 생성된다.
이런 선택을 반복하면서 최종 상태에 도달한다.
    - 올바른 선택을 계속하면 목표상태(goal state)에 도달한다.
```python
#{ 1,2,3} 집합에서 3개의 숫자를 선택하는 기본적인 예제

arr = [i for i in range(1,4)]
path = [0]*3
def backtracking(cnt):
    # 기저 조건
    # 숫자 3개를 골랐을 때 종료
    if cnt == 3:
        print(*path)
        return
    for num in arr:
        # 가지치기 - 중복된 숫자 제거
        if num in path:
            continue
        # 들어가기 전 로직
        path[cnt] = num
        # 다음 재귀 함수 호출
        backtracking(cnt+1)
        # 돌아와서 할 로직
        path[cnt] = 0
backtracking(0)

```
### 이진트리
자녀 노드가 둘 이하인 트리
1. 이진 트리 종류
    - 완전 이진 트리
        - 마지막 레벨을 제외한 모든 레벨은 꽉 차있어야 한다.
        - 마지막 레벨 노드는 왼쪽부터 채워져야 한다.
    - 포화 이진 트리
        - 모든 레벨이 꽉 차있는 것
    - 나머지 이진 트리
2. 순회 방법
    - 전위 (부모 -> 좌 -> 우)
    - 중위 (좌 -> 부모 -> 우)
    - 후위 (좌 -> 우 -> 부모)
3. 트리 저장 방법
```python
# 이것은 개발용...
# 이진트리를 전위, 중위, 후위 순회하고 방문한 노드 번호를 출력하시오

# 0. 이진트리저장
#   - 일차원 배열 저장 - 보기 어려워서 안씀
# 1. 연결 리스트로 저장 - 개발용
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    # 삽입 함수
    def insert(self, childNode):
        # 왼쪽 자식이 없을 경우
        if not self.left:
            self.left = childNode
            return
        # 오른쪽 자식이 없을 경우
        if not self.right:
            self.right = childNode
            return
        return
    # 순회
    def preorder(self):
        # 아무것도 없는 트리를 조회할 때
        if self != None:
            # 전위순회 확인 프린트
            # print(self.value, end=' ')
            # 왼쪽이 있다면 왼쪽 자식 조회
            if self.left:
                self.left.preorder()
            # 중위순회 확인 프린트
            # print(self.value, end=' ')
            # 오른쪽이 있다면 오른쪽 자식 조회
            if self.right:
                self.right.preorder()
            # 후위순회 확인 프린트
            # print(self.value, end=' ')

arr = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6]
# 이진 트리 만들기
nodes = [TreeNode(i) for i in range(0, 14)]
for i in range(0, len(arr), 2):
    parentNode = arr[i]
    childNode = arr[i+1]
    nodes[parentNode].insert(nodes[childNode])

nodes[1].preorder()

```
코테용 이진트리코드
```python
# 우리가 실제로 코테때 사용할 이진트리 코드
# 이진트리를 전위, 중위, 후위 순회하고 방문한 노드 번호를 출력하시오
arr = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6]
# 이진 트리 만들기
nodes = [[] for _ in range(0, 14)]
for i in range(0, len(arr), 2):
    parentNode = arr[i]
    childNode = arr[i+1]
    nodes[parentNode].append(childNode)

for i in range(len(nodes)):
    print(nodes[i])

# 자식이 더 이상 없다는 걸 표현하기 위해 None 을 삽입
for li in nodes:
    for _ in range(len(li), 2):
        li.append(None)

def preorder(nodeNumber):
    if nodeNumber == None:
        return
    # print(nodeNumber, end=' ')
    preorder(nodes[nodeNumber][0])
    # print(nodeNumber, end=' ')
    preorder(nodes[nodeNumber][1])
    print(nodeNumber, end=' ')

preorder(1)
```
### 서로소 집합(Disjoint-sets, Union-Find) 알고리즘
1. 상호배타 집합 표현 - 트리
```python
# 0~9
# make set - 집합을 만들어 주는 과정
# 각 요소가 가리키는 값이 부모
parent = [i for i in range(10)]

# find-set
def find_set(x):
    if parent[x] == x:
        return x
    # return find_set(parent[x])
    # 경로 압축
    parent[x] = find_set(parent[x])
    return parent[x]

# union - 같은 값으로 집합으로 묶는 법
def union(x, y):
    # 1. 이미 같은 집합인지 체크
    x = find_set(x)
    y = find_set(y)
    # 대표자가 같으니, 같은 집합이다.
    if x == y:
        return
    # 2. 다른 집합이라면, 같은 대표자로 수정
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

# union(0, 1)
union(2, 3)
union(1, 3)
# print(find_set(0))
# print(find_set(1))
# 같은 그룹인지 판별
t_x = 2
t_y = 1
if find_set(t_x) == find_set(t_y):
    print(f'{t_x} {t_y} 은 같은 집합에 속해 있습니다.')
else:
    print(f'{t_x} {t_y} 은 다른 집합에 속해 있습니다.')
print(find_set(t_x))
print(find_set(t_y))
```
### 최소 신장 트리 (MST)
우선순위 큐 사용을 위해 힙(heap) 기본적인 사용법
```python
# 우선순위 큐를 제공하는 내장라이브러리
import heapq

def prim(start):
    heap = []
    heapq.heappush(heap, (-3,2))
    heapq.heappush(heap, (-1,1))
    heapq.heappush(heap, (-2,3))
    print(type(heap))
    print(heapq.heappop(heap))
    print(heapq.heappop(heap))
    print(heapq.heappop(heap))
    print(heap)

prim(0)
```
우선순위 힙을 사용하여 선택할 수 있는 길 중에서 가중치가 제일 적은 길만 찾아 방문하기
```python
'''
prim 알고리즘
그리디를 사용해서 가장 가중치가 적은 길만 찾아 방문하기
출발정점, 도착정점, 가중치
7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''
# 우선순위 큐를 제공하는 내장라이브러리
import heapq

def prim(start):
    heap = []
    # MST 에 포함되었는지 여부
    MST = [0]*V
    # 가중치와 정점 정보
    heapq.heappush(heap, (0, start))
    # 누적합
    sum_weight = 0
    while heap:
        # 가장 적은 가중치를 가진 정점을 꺼냄
        weight, v = heapq.heappop(heap)
        # 이미 방문한 노드라면 pass
        if MST[v]:
            continue
        # 방문 체크
        MST[v] = 1
        # 누적합 추가
        sum_weight += weight
        # 갈 수 있는 노드들을 체크
        for next in range(V):
            # 갈 수 없거나 이미 방문했다면 pass
            if graph[v][next] == 0 or MST[next]:
                continue
            heapq.heappush(heap, (graph[v][next], next))
    return sum_weight

V, E = map(int, input().split())
# 인접행렬
graph = [[0]*V for _ in range(V)]
for _ in range(E):
    f, t, w = map(int, input().split())
    graph[f][t] = w
    graph[t][f] = w  # 무방향 그래프, 정보를 3개 담기위해 인접 리스트말고 행렬사용
result = prim(0)
print(f'최소 비용은 {result}이다.')
```
위와 같은 문제, 우선순위 힙 말고 유니온 파인드 sort를 사용해서 풀기
```python
'''
7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''
V, E = map(int, input().split())
edge = []
for _ in range(E):
    f, t, w = map(int, input().split())
    edge.append([f, t, w])
# w 를 기준으로 정렬
edge.sort(key=lambda x: x[2])
# 사이클 발생 여부를 union find로 해결
parents = [i for i in range(V)]

def find_set(x):
    if parents[x] == x:
        return x
    parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    x = find_set(x)
    y = find_set(y)
    if x == y:
        return
    if x < y:
        parents[y] = x
    else:
        parents[x] = y

# 현재 방문한 정점 수
cnt = 0
sum_weight = 0
for f, t, w in edge:
    # 싸이클이 발생하지 않는 다면
    if find_set(f) != find_set(t):
        cnt += 1
        sum_weight += w
        union(f, t)
        # MST 구성이 끝나면
        if cnt == V:
            break
print(f'최소 비용은 {sum_weight}이다.')
```
### 최단 경로 정의
하나의 시작 정점에서 끝 정점까지의 최단 경로
1. 다익스트라(dijkstra) 알고리즘
    - 음의 가중치를 허용하지 않음
2. 벨만-포드(Bellman-Ford) 알고리즘
    - 음의 가중치를 허용
3. 플로이드-워샬(Floyd-Warshall) 알고리즘
    - 모든 정점들에 대한 최단 경로
### 다익스트라(dijkstra)
내가 도달해야 하는 위치까지 가장 최단거리로 도달할 수 있는 알고리즘
```python
'''
6 8
0 1 2
0 2 4
1 2 1
1 3 7
2 4 3
3 4 2
3 5 1
4 5 5
'''
# 최단 거리 문제 유형
# 1. 특정 지점 -> 도착 지점까지의 최단 거리 : 다익스트라
# 2. 가중치에 음수가 포함되어 있다면 다익스트라를 사용해서는 안된다. 밸만포드 사용하자
# 3. 여러 지점 -> 여러 지점까지의 최단 거리 : 플로이드-워샬
#     - 여러지점 다익스트라 돌리기 그러나 시간 복잡도 계산 잘해야함
# 내가 갈 수 있는 경로 중 누적거리가 제일 짧은 것부터 고르자
import heapq
# 입력
n, m = map(int, input().split())
# 인접리스트
graph = [[] for i in range(n)]
for _ in range(m):
    f, t, w = map(int, input().split())
    graph[f].append([t,w])
# 1. 누적 거리를 계속 저장
INF = int(1e9) # 최대값으로 1억 -  대충 엄청 큰 수
distance = [INF] *n

def dijkstra(start):
    # 2. 우선순위 큐
    pq = []
    # 출발점 초기화
    heapq.heappush(pq, (0,start))
    distance[start] = 0
    while pq:
        # 누적 거리가 가장 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(pq)
        # 이미 방문한 지점 + 누적 거리가 더 짧게 방문한 적이 있다면 pass
        if distance[now] < dist:
            continue
        # 인접 노드를 확인
        for next in graph[now]:
            next_node = next[0]
            cost = next[1]
            # next_node 로 가기 위한 누적 거리
            new_cost = dist + cost
            # 누적거리가 기존보다 크다면
            if distance[next_node] <= new_cost:
                continue
            distance[next_node] = new_cost
            heapq.heappush(pq, (new_cost, next_node))
dijkstra(0)
print(distance)
```
### 알고리즘 마지막주에 배운 내용
**앞으로 혼자 공부해야하는 내용**
1. 그래프 탐색
    - 완전 탐색 : DFS, BFS
2. 서로소 집합
    - 대표 데이터 비교
    - 그래프에서는 싸이클 판별
3. 최소 비용
    - 최소 신장 트리(MST)
        - 전체 그래프에서 총합이 최소인 신장 트리
    - 최단 거리(다익스트라)
        - 정점 사이의 거리가 최단인 경로 찾기