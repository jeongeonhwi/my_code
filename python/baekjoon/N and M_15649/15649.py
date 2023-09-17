import sys
sys.stdin = open('input.txt', 'r')


def permutation(start, end):
    if start == end:
        for e in range(end-1):
            if p[e] > p[e+1]:
                return
        print(*p)
        return
    else:
        for j in range(start, N):
            if used[j] == 0:
                p[start] = numbers[j]
                used[j] = 1
                permutation(start+1, end)
                used[j] = 0


N, M = map(int, input().split())
numbers = []
for i in range(1, N+1):
    numbers.append(i)
used = [0]*N
p = [0]*M
permutation(0, M)