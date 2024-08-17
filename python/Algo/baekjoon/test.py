a,b = input().split()
a = list(a)
b = list(b)
a.reverse()
b.reverse()
ai = list(map(int, a))
bi = list(map(int, b))
ans = []
for i in range(max(len(ai), len(bi))):
    if i<min(len(ai), len(bi)):
        ans.append(ai[i]+bi[i])
    else:
        if len(ai)>len(bi):
            ans.append(ai[i])
        else:
            ans.append(bi[i])

for i in range(len(ans)-1):
    if ans[i] >= 2:
        ans[i] -= 2
        ans[i+1] += 1
else:
    if ans[-1] >= 2:
        ans[-1] -= 2
        ans.append(1)
if sum(ans) == 0:
    print(0)
else:
    while True:
        if ans[-1] == 0:
            ans.pop()
        else:
            break
    ans.reverse()
    for i in ans:
        print(i, end="")