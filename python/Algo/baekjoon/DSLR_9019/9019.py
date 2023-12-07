import sys
# sys.stdin = open('input.txt', 'r')


from collections import deque

def make_D(A):
    A = A*2%10000
    return A


def make_S(A):
    A = (A-1)%10000
    return A


def make_L(A):
    A = A//1000 + (A%1000)*10
    return A


def make_R(A):
    A = A//10+(A%10)*1000
    return A


def bfs(A):
    visited = [0]*10001
    q = [[A,'']]
    visited[A] = 1
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
    A, B = list(map(int, input().split()))
    ans = bfs(A)
    print(ans)
