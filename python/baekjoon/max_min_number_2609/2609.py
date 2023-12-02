a, b = map(int, input().split())

alist = [0]*max(a+1,b+1)
blist = [0]*max(a+1,b+1)
max_v = 0
while True:
    for i in range(2, 100000):
        if a%i == 0:
            alist[i] += 1
            a //= i
            max_v = max(i, max_v)
            break
    if a <= 1:
        break

while True:
    for i in range(2, 100000):
        if b%i == 0:
            blist[i] += 1
            b //= i
            max_v = max(i, max_v)
            break
    if b <= 1:
        break

max_ans = 1
min_ans = 1

for i in range(max_v+1):
    if alist[i] == 0 and blist[i] == 0:
        continue
    max_ans *= max(i**alist[i], i**blist[i])
    if alist[i] == 0 or blist[i] == 0:
        continue
    min_ans *= min(i**alist[i], i**blist[i])
print(min_ans)
print(max_ans)
