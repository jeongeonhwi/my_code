import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')


N,M = map(int, input().split())
arr = list(map(int, input().split()))

aset = set()
bset = set()
pi = 0
pj = 1
while pj<=N:
    if sum(arr[pi:pj]) == M:
        aset.add(pi)
        pi = pj
        pj += 1
    elif sum(arr[pi:pj]) > M:
        pi = pj
        pj += 1
    else:
        pj += 1
for i in range(N):
    if i in aset:
        continue
    # for j in range(i+1,N):
        # if sum(arr[i:j])%M == 0:

print(aset)