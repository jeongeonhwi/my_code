import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for _ in range(T):
    N = int(input())
    fake = [[0]*1001 for _ in range(1001)]
    i_idx = []
    j_idx = []
    i_len = []
    j_len = []
    for k in range(1, N+1):
        j1, i1, w, h = map(int, input().split())
        for i in range(i1, i1+h):
            for j in range(j1, j1+w):
                fake[i][j] = k
        i_idx.append(i1)
        j_idx.append(j1)
        j_len.append(j1+w)
        i_len.append(i1+h)

    i_idx.sort()
    j_idx.sort()
    i_len.sort()
    j_len.sort()
    num = []
    for i in range(1, N+1):
        num.append(i)
    result = [0]*N
    for k in range(N):
        for i in range(i_idx[0], i_len[-1]):
            for j in range(j_idx[0], j_len[-1]):
                if fake[i][j] == num[k]:
                    result[k] += 1
    for i in range(N):
        print(result[i])