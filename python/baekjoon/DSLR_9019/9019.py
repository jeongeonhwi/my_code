import sys
sys.stdin = open('input.txt', 'r')


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
    A = A[1:] + A[0]
    A = ''.join(A)
    return A


def make_R(A):
    A = list(A)
    tmp = [A.pop()]
    A = tmp + A
    A = ''.join(A)
    return A


def per(start, end):
    




T = int(input())
for tc in range(1, T+1):
    A, B = list(input().split())
    print(A)
    print(B)
