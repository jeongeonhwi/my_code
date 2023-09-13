import sys
sys.stdin = open('input.txt', 'r')


from collections import deque

def make_D(A):
    A = int(A)
    A = A*2
    if A > 9999:
        A = A%10000
    return str(A)


def make_S(A):
    A = int(A)
    if A == 0:
        A = 9999
    else:
        A -= 1
    return str(A)


def make_L(A):
    A = list(A)
    A = deque(A)
    tmp = A.popleft()
    A.append(tmp)
    if len(A) > 1:
        A = ''.join(A)
    else:
        A = A[0]
    A = int(A)
    A = str(A)
    return A


def make_R(A):
    A = list(A)
    tmp = [A.pop()]
    A = tmp + A
    if len(A) > 1:
        A = ''.join(A)
    else:
        A = A[0]
    A = int(A)
    A = str(A)
    return A


def bfs(A):
    visited = [0]*10002
    q = [[A,'']]
    visited[int(A)] = 1
    q = deque(q)
    while True:
        i,j = q.popleft()
        if i == B:
            return j
        tmp = j
        if  visited[int((make_R(i)))] == 0:
            j = tmp + 'R'
            q.append((make_R(i),j))
            visited[int((make_R(i)))] = 1
        if  visited[int((make_L(i)))] == 0:
            j = tmp + 'L'
            q.append((make_L(i),j))
            visited[int(make_L(i))] = 1
        if  visited[int(make_S(i))] == 0:
            j = tmp + 'S'
            q.append((make_S(i),j))
            visited[int(make_S(i))] = 1
        if  visited[int((make_D(i)))] == 0:
            j = tmp + 'D'
            q.append((make_D(i),j))
            visited[int(make_D(i))] = 1




T = int(input())
for tc in range(1, T+1):
    A, B = list(input().split())
    ans = bfs(A)
    print(ans)
