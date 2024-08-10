a,b = map(int, input().split())
alist = []
blist = []
ans = 0
while a!=0 or b!=0:
    if a>0:
        tmp = a%10
        a //= 10
        alist.append(tmp)
    if b>0:
        tmp = b%10
        b //= 10
        blist.append(tmp)

for i in alist:
    for j in blist:
        ans += (i*j)
print(ans)
