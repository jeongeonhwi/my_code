import sys
sys.stdin = open('input.txt', 'r')


def double_permutation(start, end, k):
    if start == k:
        for i in range(M-1):
            if p[i] > p[i+1]:
                return
        print(*p)
        return
    for j in range(N):
        p[start] = arr[j]
        double_permutation(start+1, end, k)


N,M = map(int, input().split())
arr = [i for i in range(1, N+1)]
p = [0]*M
double_permutation(0,N,M)