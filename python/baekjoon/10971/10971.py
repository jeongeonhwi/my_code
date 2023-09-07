import sys
sys.stdin = open('input.txt')



def per(i, K):
    global min_v
    if i == K:
        c = [0] + p[:] + [0]
        tmp = 0
        for cnt in range(len(c)-1):
            if arr[c[cnt]][c[cnt+1]] != 0:
                tmp += arr[c[cnt]][c[cnt+1]]
            else:
                return
        min_v = min(min_v, tmp)
        return
    else:
        for j in range(K):
            if not used[j]:
                used[j] = 1
                p[i] = num[j]
                per(i+1, K)
                used[j] = 0


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
min_v = float('inf')
num = []
for i in range(1, N):
    num.append(i)
K = N-1
used = [0]*K
p = [0]*K
per(0, K)
print(min_v)

