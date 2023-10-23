
def fib(N):
    global cnt1
    if N == 1 or N == 2:
        cnt1 += 1
        return 1
    else:
        return fib(N-1) + fib(N-2)


N = int(input())
nlist = [0]*(N+1)
cnt1 = 0
cnt2 = 0
fib(N)
nlist[1], nlist[2] = 1, 1
for i in range(2, N):
    cnt2+=1
    nlist[i] = nlist[i-1]+nlist[i-2]
print(cnt1,cnt2)
