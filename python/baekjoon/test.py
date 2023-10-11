def per(start, end, k):
    global percnt
    if start == k:
        percnt+=1
        print(p)
        return
    for j in range(N):
        if used[j] == 0:
            p[start] = arr[j]
            used[j] = 1
            per(start+1, end, k)
            used[j] = 0






arr = [0,1,2,3,4,5,6,7,8,9]
N = 10
bitcnt = 0
for i in range(1<<N):
    group = []
    # print(i)
    for j in range(N):
        # print(j)
        if i & (1<<j):
            # print(i & (1<<j))
            group.append(arr[j])
        bitcnt+= 1
    if len(group) != 3:
        continue

print(bitcnt)

percnt = 0
p = [0]*N
used = [0]*N
per(0,N, 5)
print(percnt)