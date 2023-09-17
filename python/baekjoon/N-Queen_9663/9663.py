def permutation(start, end):
    global cnt
    if start == end:
        cnt += 1
        return
    else:
        for j in range(N):
            if used[j] == 0:
                p[start] = numbers[j]
                used[j] = 1
                permutation(start+1, end)
                used[j] = 0

di = [1, -1, 0, 0, 1, -1, -1, 1]
dj = [0, 0, 1, -1, 1, 1, -1, -1]

N = int(input())
arr = [[1]*N for _ in range(N)]
for i in 
numbers = []
for i in range(1, N+1):
    numbers.append(i)
used = [0]*N
p = [0]*N
cnt = 0
permutation(0, N)
print(cnt)