a = [i for i in range(25)]
N = 15
cnt = 0
for i in range(1<<N):
    for j in range(N):
        if i&(1<<j):
            cnt +=1
    if len(a) > 5 or len(a) == 0:
        continue
    # 여기서부터 코드진행
print(cnt)

cnt2 = 0
p = [0]*5
used = [0]*N
k = 5

def permutation(start, end, k):
    global cnt2
    cnt2 +=1
    if start == k:
        return
    for j in range(N):
        if used[j] == 0:
            used[j] = 1
            p[start] = a[j]
            permutation(start+1, end, k)
            used[j] = 0

permutation(0,N,k)
print(cnt2)

a = 25+25*24+25*24*23+25*24*23*22+25*24*23*22*21
print(a)